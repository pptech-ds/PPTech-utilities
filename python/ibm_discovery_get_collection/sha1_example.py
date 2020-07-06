def existing_sha1s(discovery,
                   environment_id,
                   collection_id):
    """
    Return a list of all of the extracted_metadata.sha1 values found in a
    Watson Discovery collection.

    The arguments to this function are:
    discovery      - an instance of DiscoveryV1
    environment_id - an environment id found in your Discovery instance
    collection_id  - a collection id found in the environment above
    """
    sha1s = []
    alphabet = "0123456789abcdef"   # Hexadecimal digits, lowercase
    chunk_size = 10000

    def maybe_some_sha1s(prefix):
        """
        A helper function that does the query and returns either:
        1) A list of SHA1 values
        2) The `prefix` that needs to be subdivided into more focused queries
        """
        response = discovery.query(environment_id,
                                   collection_id,
                                   {"count": chunk_size,
                                    "filter": "extracted_metadata.sha1::"
                                              + prefix + "*",
                                    "return": "extracted_metadata.sha1"})
        if response["matching_results"] > chunk_size:
            return prefix
        else:
            return [item["extracted_metadata"]["sha1"]
                    for item in response["results"]]

    prefixes_to_process = [""]
    while prefixes_to_process:
        prefix = prefixes_to_process.pop(0)
        prefixes = [prefix + letter for letter in alphabet]
        # `pmap` here does the requests to Discovery concurrently to save time.
        results = pmap(maybe_some_sha1s, prefixes, threads=len(prefixes))
        for result in results:
            if isinstance(result, list):
                sha1s += result
            else:
                prefixes_to_process.append(result)

    return sha1s