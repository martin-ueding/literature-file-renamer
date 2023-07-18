from literature_file_renamer.names import clean_name


def test_clean_name() -> None:
    input = """

  
    1.Feathers, M. Working Effectively with Legacy Code. (Pearson, 2004).
  

"""
    expected = "Feathers, M. Working Effectively with Legacy Code. (Pearson, 2004)"
    assert clean_name(input) == expected


def test_clean_name_preprint() -> None:
    input = """

  
    1.Dao, T., Fu, D. Y., Ermon, S., Rudra, A. & Ré, C. FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. Preprint at https://doi.org/10.48550/arXiv.2205.14135 (2022).
  

"""
    expected = "Dao, T., Fu, D. Y., Ermon, S., Rudra, A. & Ré, C. FlashAttention. Fast and Memory-Efficient Exact Attention with IO-Awareness. (2022)"
    assert clean_name(input) == expected
