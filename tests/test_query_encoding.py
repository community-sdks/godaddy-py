from godaddy_python import ApiClient

def test_build_query_pairs_repeats_keys_for_arrays():
    assert ApiClient.build_query_pairs([("items", ["a", "b"])]) == [("items", "a"), ("items", "b")]
