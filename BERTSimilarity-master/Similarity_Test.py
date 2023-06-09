# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:48:13 2020

@author: Abhilash
"""

import BertSimilarity.BERTSimilarity as bertsimilarity
import copy
'''
This is a sample example of checking similarity between 2 sentences.
This takes as inputs 2 sentences (strings).
The BertSimilarity() class is instantiated and then the calculate_distance() method
is called, which computes the distance (cosine).
'''

if __name__=='__main__':
    bertsimilarity = bertsimilarity.BERTSimilarity()
    print('load done')

    s1 = 'The Commission has also stepped up its planned support for regional cooperation projects between Israelis and Arabs. We committed more than EUR 20 million for such projects last year. This package included renewed assistance for people to people activities and cross border cooperation where Israelis and Arabs meet on no governmental and expert levels. Members will recall that the European Union is the largest financial donor to the overall efforts in bringing reconciliation to the people of the Middle East. The Commission has also stepped up its planned support for regional cooperation projects between Israelis and Arabs. We committed more'
    s2 = 'It is already apparent that the financial resources currently available for Community assistance to this part of the world will not be sufficient for the magnitude of support that will be required in the event of permanent peace. I want to underline that point. I wish insistently to remind the Council and, should it be necessary, Parliament, that we should not continue to allow a gap to develop between our rhetoric and what we are actually capable of doing. I repeat that a change in the politics of the Middle East will require a gear change in the support that'
    s3 = 'We have made progress in recent months and weeks, as Mr Gama mentioned earlier. But it is inevitably going to be a tough process with difficulties and disappointments on the way. We will do all we can to help the process to a successful conclusion and to meet the obligations and challenges that will be created by that outcome. Lastly, I will repeat for some who have entered the Chamber in the last few minutes, what I said at the outset of my remarks, that I will not be able to stay until the end of the debate, largely as'
    s4 = 'The statements we have heard today on the Middle East peace process are very opportune at the moment because of the hurried tour which Minister Gama whose absence from this debate I also regret has made of the region, accompanied by other Council representatives. The tone of the news in the media on the recent events in the area could lead us to take a pessimistic view of the situation. I honestly believe that an evaluation of this type would not be in accordance with the reality of that situation. In this sense I share positive attitude of Commissioner Patten.'
    s5 = 'Let me explain, it is true that the Israeli Government has delayed the third hand over of West Bank territory to the Palestinian authorities. This is naturally on the condition that the delay does not exceed three weeks, as Prime Minister Barak has promised. On the other hand, the decision to delay the second round of talks, initiated in Shepherdstown by the Syrian Arab Republic, is undoubtedly significant, but I am convinced that the hopes which were raised on 3 January in that town will not be dashed. In my judgement, this constitutes a guarantee to both sides, both from'
    s6 = 'While the negotiations on the final peace settlement have begun, I think it is important to keep the two processes apart. A lack of progress in the final status negotiations should not jeopardise implementation of the three above-mentioned interim agreements. What we need to look out for in this context is how matters develop in connection with the harbours in Gaza, the northern transit route between Gaza and the West Bank, further releases of political prisoners and implementation of the financial commitments. The second point relates to Syria. There, the border question is obviously central. How negotiations are proceeding there'
    s7 = 'The third aspect is the peace negotiations in Syria which are closely linked to the issue of Israeli withdrawal from Southern Lebanon. According to UNIFIL, there are now concrete signs that Israel is preparing to withdraw, which is something we welcome. There too, of course, outstanding matters in dispute are the water problem and the situation of the Lebanese Palestinian refugees. Mr President, I would like to refer, firstly and above all, to the joint resolution which will be laid down to round off this debate. My Group has made a contribution to this resolution and, needless to say, approves '
    s8 = 'In addition to the bilateral meetings with Syria, I hope that Israel will also enter into negotiations with Lebanon within the foreseeable future and that, in the framework of economic and regional cooperation, a multilateral approach will appear possible. Nevertheless, it is still regrettable that the European Union, one of the most important financial donors, is still unable to play a major political role in the peace process. This is where Mr Solana, the High Representative to the Council, could come into his own. The Commission and Member States also have to be encouraged to support projects which can help'
    s9 = 'It is high time there was peace in the Middle East. It is time to end the era which began with the Balfour declaration in 1917. It is time there were secure borders and political, social and economic rights in every country in this region, and that human rights were recognised and upheld in Syria, Palestine, Israel and everywhere else. This is an exercise in sovereignty, and in democracy for each population and every individual, but to this end it is vital for all parties in the conflict to have the courage to strive for peace and rights, and to recognise the other as its partner and not as its subject to whom concessions must be given. '
    s10 = 'I refer principally to the Palestine Israel question, but the same also applies to the territories which have been occupied in the Golan since 1967 and in southern Lebanon since 1982. Israel has to accept its responsibilities, withdraw from the occupied territories and share its water resources but, at the same time, it has to be sure that it will be safe and able to live in peace in terms of economic and political relations with all the countries in the area. However, Israel is not the only country concerned with security. The same goes for the other countries, especially'

    f1 = s5
    words = f1.split()
    temp = copy.deepcopy(words)
    i = 0
    x = []
    for j in range(20):
        del temp[i:i + 5]
        x.append(temp)
        temp = copy.deepcopy(words)
        i += 5

    Dist = []
    for k in range(20):
        f2 = " ".join(x[k])
        dist=bertsimilarity.calculate_distance(f1,f2)
        # print('The distance between sentence1: '+f1+' and sentence2: '+f2+' is '+str(dist))
        print(k)
        Dist.append(1-dist)
    print(Dist)

    # # f1='The company forecasted a profit of 10%'
    # # f2='The F1 company did not loose the race in England'
    # # f3='The Titanic sank in the Atlantic Ocean'
    # # f4='The Pacific Ocean is deeper in the Atlantic Ocean'
    # # d1=bertsimilarity.calculate_distance(f1,f2)
    # # d2=bertsimilarity.calculate_distance(f1,f3)
    # # d3=bertsimilarity.calculate_distance(f3,f4)
    # # d4=bertsimilarity.calculate_distance(f1,f4)
    # # print('The distance between sentence1: '+f1+' and sentence2: '+f2+' is '+str(d1))
    # # print('The distance between sentence1: '+f1+' and sentence3: '+f3+' is '+str(d2))
    # # print('The distance between sentence3: '+f3+' and sentence4: '+f4+' is '+str(d3))
    # # print('The distance between sentence1: '+f1+' and sentence4: '+f4+' is '+str(d4))