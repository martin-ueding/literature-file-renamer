from literature_file_renamer.names import clean_name


examples = {
    """

  
    1.Su, J. et al. RoFormer: Enhanced Transformer with Rotary Position Embedding. Preprint at https://doi.org/10.48550/arXiv.2104.09864 (2022).
  

""": "Su, J. et al. RoFormer. Enhanced Transformer with Rotary Position Embedding. (2022)",
    """

  
    1.Feathers, M. Working Effectively with Legacy Code. (Pearson, 2004).
  

""": "Feathers, M. Working Effectively with Legacy Code. (Pearson, 2004)",
    """

  
    1.Dao, T., Fu, D. Y., Ermon, S., Rudra, A. & Ré, C. FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. Preprint at https://doi.org/10.48550/arXiv.2205.14135 (2022).
  

""": "Dao, T., Fu, D. Y., Ermon, S., Rudra, A. & Ré, C. FlashAttention. Fast and Memory-Efficient Exact Attention with IO-Awareness. (2022)",
}


def test_clean_name() -> None:
    for input, expected in examples.items():
        assert clean_name(input) == expected
