#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   vocab.py
@Time    :   2022/02/21 23:46:31
@Author  :   DiosGuo 
@Version :   1.0
@Contact :   943024256@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   Vocab Builder
'''
from typing import Iterable, Callable
from collections import defaultdict
from tqdm import tqdm 


class Vocab(object):
    """
    用于构建词典，获得将字符串和idx相互转换的方法
    """
    def __init__(self, max_size=2000, max_freq=-1, min_freq=1, tokinzer:Callable=None) -> None:
        """初始化词典

        Args:
            max_size (int, optional): 词典的最大的大小. Defaults to 2000.
            max_freq (int, optional): 语料中保留的词的最大词频. Defaults to -1.
            min_freq (int, optional): 保留到词典中的最小词频. Defaults to 1.
            tokinzer (Callable, optional): 分词方法. Defaults to None.
        """

        super().__init__()
        self._max_size = max_size
        if max_freq == -1:
            max_freq = float('inf')
        self._max_freq = max_freq 
        self._min_freq = min_freq 
        self._tokinzer = tokinzer 

        self._word2idx = {}
        self._idx2word = {}

        self._term_counter = defaultdict(int)

    def _init_param(self):
        self._word2idx = {'<pad>':0, '<unk>':1}
        self._idx2word = {0:'<pad>', 1:'<unk>'}

    def fit(self, corpus) -> None :
        self._init_param()

        for document in tqdm(corpus, desc='vocab building:'):
            if self._tokinzer is not None:
                document = self._tokinzer(document)
            for term in document:
                self._term_counter[term] += 1 
        
        sorted_term_info_list = sorted(
            [(k,v) for k, v in self._term_counter.items() if self._max_freq > v > self._min_freq],
            key=lambda x:x[1]
        )
    
        for term, _ in sorted_term_info_list[:self._max_size]:
            self._word2idx[term] = len(self._word2idx)
            self._idx2word[len(self._word2idx) - 1] = term 

    @property
    def size(self):
        return len(self._word2idx)

    def transform(self, corpus):
        """将输入的文字Corpus转换为ID的形式

        Args:
            corpus (_type_): 输入的语料

        Returns:
            _type_: 输出的id形式语料
        """
        transformed_corpus = []
        for document in corpus:
            transformed_document = []
            for term in document:
                if term in self._word2idx:
                    transformed_document.append(self._word2idx[term])
                else:
                    transformed_document.append(self._word2idx['<unk>'])
            transformed_corpus.append(transformed_document)
        return transformed_corpus

    def reverse(self, corpus_idx):
        ...

    def save(self, path):
        ... 

    def load(self, path):
        ...

    @classmethod
    def load_from(cls, path):
        ...
