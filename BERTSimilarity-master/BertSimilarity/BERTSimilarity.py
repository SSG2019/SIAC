# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:42:34 2020

@author: Abhilash
"""

import torch
# from pytorch_pretrained_bert import
from transformers import BertTokenizer,BertModel
from scipy.spatial.distance import cosine

'''
A Simple library for extracting BERT embeddings through forward pass only.
The hidden layers are stacked and the sum of the torch vectors are taken.
Average pooling is applied as recommended by Devlin etal.
Original paper :https://arxiv.org/abs/1810.04805
Source code for BERT by Google Research:https://github.com/google-research/bert/
The base pytorch wrapper is taken from Chris McCormick:https://github.com/chrisjmccormick
'''



class BERTSimilarity():
    def bert_tokenize(self,data):
        self.data=data
        self.output_tokens=''
        self.output_tokens+='[CLS] ' +self.data+' [SEP]'
        return self.output_tokens
    def sentential_embeddings(self,tokenizer,tokenized_text):
        self.tokenizer=tokenizer
        self.tokenized_text=tokenized_text
        self.idx_tokens=self.tokenizer.convert_tokens_to_ids(self.tokenized_text)
        self.segmenter_idx=[1]*len(self.tokenized_text)
        self.tokens_tensor=torch.tensor([self.idx_tokens])
        self.segmenter_tensor=torch.tensor([self.segmenter_idx])
        self.model=BertModel.from_pretrained('bert-base-uncased',output_hidden_states=True)
        self.model.eval()
        with torch.no_grad():
            self.outputs=self.model(self.tokens_tensor,self.segmenter_tensor)
            self.hidden_state=self.outputs[2]
        self.token_vecs=self.hidden_state[-2][0]
        self.sentence_embeddings=torch.mean(self.token_vecs,dim=0)
        return self.sentence_embeddings
    def calculate_distance(self,sentence_1,sentence_2):
        self.sentence_1=sentence_1
        self.sentence_2=sentence_2
        self.tokenizer=BertTokenizer.from_pretrained('bert-base-uncased')
        self.preprocess_1=self.bert_tokenize(self.sentence_1)
        self.preprocess_2=self.bert_tokenize(self.sentence_2)
        self.tokenized_text_1=self.tokenizer.tokenize(self.preprocess_1)
        self.tokenized_text_2=self.tokenizer.tokenize(self.preprocess_2)
        self.sentence_1 =self.sentential_embeddings(self.tokenizer,self.tokenized_text_1)
        self.sentence_2 =self.sentential_embeddings(self.tokenizer,self.tokenized_text_2)
        self.distance=1-cosine(self.sentence_1,self.sentence_2)
        return self.distance