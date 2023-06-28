# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:48:13 2020

@author: Abhilash
"""

import BertSimilarity.BERTSimilarity as bertsimilarity
import copy
import time
'''
This is a sample example of checking similarity between 2 sentences.
This takes as inputs 2 sentences (strings).
The BertSimilarity() class is instantiated and then the calculate_distance() method
is called, which computes the distance (cosine).
'''

if __name__=='__main__':
    bertsimilarity = bertsimilarity.BERTSimilarity()
    print('load done')

    s1 = 'In the Conference of Presidents, we had an in depth discussion. Your Group was alone in advocating what you are saying now. We then put it to a vote. As you know, each chairman has the same number of votes as his Group has Members. There was a vote on this matter. As I recall, the outcome of this vote was 422 votes to 180 with a few abstentions. This means that all the Groups with the exception of the nonattached Members but, of course, they are not a Group were in agreement; only your Group thought that we should'
    s2 = 'The Commission will present its programme for the year 2000 in February. We have said, very well, if the Commission does not wish to introduce the 2000 programme as early as January then we will do it in February. We have agreed to this. After all, we do not wish to quarrel with the Commission; if at all possible, we believe that the Commission and Parliament need to tread the same path. However, we in Parliament also have a supervisory role with regard to the Commission and we do not have to agree with everything which comes out of the'
    s3 = 'I should like us to be able to do a reasonable amount of preparation for the debate on the five year programme in our Groups. You cannot prepare if you hear a statement in this House and have no idea of its content. That is why we would recommend and it is my impression that the Commission is also open to this idea that we hold the debate on the long term programme of Commissions up to the year 2005 in February and I hope that the Commission will agree on a programme before then which it will propose to '
    s4 = 'Madam President, I would like to say that the agreement reached in September distinguished this debate from the annual presentation of the Commission legislative programme. I would also like to say that the Commission is prepared and ready to hold this debate whenever it is convenient and that we were ready to do so this week as we had agreed originally, on the basis that it would be presented the day before in a speech to parliamentary groups. Therefore, Madam President, I would like to repeat that the Commission has debated the action plan for the next five years'
    s5 = 'I propose that we vote on the request of the Group of the Party of European Socialists that the Commission statement on its strategic objectives should be reinstated. I have another proposal regarding the oral question on capital tax. The Group is requesting that this item be taken off the agenda. Is there a member who wishes to speak on behalf of this Group to propose this? Madam President, I can hear a ripple of laughter from the Socialists. I was told that large sections of the Socialist Group were also keen to have this item taken off the agenda'
    s6 = 'because at the vote in the Conference of Presidents no vote was received from the working group of Members of the Socialist Group responsible for this matter. I do not know whether this information is correct, but the Group would, in any case, be grateful if this item were removed because Parliament has addressed this issue several times already. Decisions have also been adopted against a tax of this kind. That is why my Group moves that this item be taken off the agenda. Thank you, Mr Poettering. We shall now hear Mr Wurtz speaking against this request. I do.'
    s7 = 'we cannot and must not accept the fact that we hear ever more frequently of accidents causing major damage on our roads, but also on our railways and waterways, not solely but at least partly because those involved do not take the transport of dangerous goods seriously enough or because as a result of ignorance or a lack of training on the part of the drivers or others responsible for the various vehicles a minor accident has all too often become a major disaster. As an Austrian, I still have a vivid memory, as, I believe, we all do, of'
    s8 = 'I should like to address one final point. We must not content ourselves with sealing another hole in the safety net and shutting our eyes to the fact that, where transport safety in Europe is concerned, there is still much more to be done. In this context, I should like to make a request and ask the Commissioner responsible, who is with us here today, to table an appropriate text as soon as possible with a view to continuing to make it safer for traffic to transit tunnels in the future, so that we in Europe do not have to'
    s9 = 'The work is done. All that remains is the business of enforcement. I would like to mention one final point. With regard to enforcement, proper agreements must also be concluded with the Eastern European countries because they will not enter into treaties which deal with this matter until 1 July 2001, that is to say in eighteen months time. This gives them a competitive edge for the interim period. This is not in itself anything dreadful, but we should prioritise particularly the safety aspects for goods transported by road, rail and inland waterways and incorporate these, as part of the'
    s10 = 'My second point has already been mentioned, it concerns the minimum standards. In principle, I believe that in many cases where transport is concerned we should be working towards increased flexibility and country specific rules. However, when it comes to safety, I am rather sceptical because safety in Sweden, for example, is in principle no different from safety in Germany, Italy or Austria. I can live with these minimum standards, but I would ask the Commission to monitor the situation very carefully. Should flexibility of this kind result in there being inadequate rules in some countries then we should work'

    for m in [s1, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]:

        f1 = m
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
        T = 0
        for k in range(20):
            f2 = " ".join(x[k])
            start_time = time.time()
            dist=bertsimilarity.calculate_distance(f1,f2)
            end_time = time.time()
            T += end_time - start_time
            # print('The distance between sentence1: '+f1+' and sentence2: '+f2+' is '+str(dist))
            print(k)
            Dist.append(1-dist)
        print(Dist)
        print(T)


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