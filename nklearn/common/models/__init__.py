#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2022/01/22 23:34:28
@Author  :   DiosGuo 
@Version :   1.0
@Contact :   raogx.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   TextCNN Model: Kim, Y. . (2014). Convolutional neural networks for sentence classification. Eprint Arxiv.
'''


from torch import nn 


class TextCNN(nn.Module):

    def __init__(self, 
            vocab_size:int, 
            emb_size:int,
            kernel_size:list=None, 
            output_kernel:list=None,
            stride:list=None,
            emb_weights:list=None,
            padding_idx: int=0
        ):
        self.vocab_size = vocab_size
        self.emb_size = emb_size
        self.padding_idx = padding_idx
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, emb_size, padding_idx=padding_idx)

        self.cnn = nn.Conv1d(1, 3, kernel_size, stride, padding_mode)

    def forward(self, inputs):
        ... 

