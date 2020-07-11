## Revealing the Hidden Links in Content Networks: An Application to Event Discovery (ACM CIKM 2017)
#### Authors: [Antonia Saravanou](http://cgi.di.uoa.gr/~antoniasar/), [Ioannis Katakis](http://www.katakis.eu/), [George Valkanas](http://cgi.di.uoa.gr/~gvalk/), [Vana Kalogeraki](http://www2.cs.aueb.gr/~vana/), [Dimitrios Gunopulos](http://kddlab.di.uoa.gr/dg.html)
#### [Link to the paper](http://cgi.di.uoa.gr/~antoniasar/papers/Saravanou_HiddenLinks_CIKM2017.pdf)
#### [Link to the poster](http://cgi.di.uoa.gr/~antoniasar/papers/Saravanou_HiddenLinks_CIKM2017_poster.pdf)

### Introduction
Social networks have become the de facto online resource for people to share, comment on and be informed about events pertinent to their interests and livelihood, ranging from road traffic or an illness to concerts and earthquakes, to economics and politics. In this paper, we focus on how Social Networks can help us identify events effectively. Content Networks incorporate both structural and content-related information of a Social Network in a unified way, at the same time, bringing together two disparate lines of research: graph-based and content-based event discovery in social media. 

We model interactions of two types of nodes, users and content, and introduce an algorithm that builds heterogeneous, dynamic graphs, in addition to revealing content links in the network’s structure. By linking similar content nodes and tracking connected components over time, we can effectively identify different types of events. Our evaluation on social media streaming data suggests that our approach outperforms state-of-the-art techniques, while showcasing the significance of hidden links to the quality of the results

**LiCNo** (**Li**nking **C**ontent **No**des) is an event detection framework that utilizes a novel representation that considers both the content and the structure of a social network. More specifically, we model the streaming data as a dynamic, heterogeneous graph. Our approach treats large connected components of this graph as indicators of events. The intuition is that when there are a lot of users who either directly interact with each other (as seen with the network structure) or, indirectly, talk about similar topics (based on the text similarity), then these users form large connected components.

The contributions of this work can be summarized as follows:
1. **Network Representation**: We introduce a novel representation of a network as a dynamic heterogeneous graph, the Content Network. 
2. **Revealing Hidden Links**: We provide an algorithm that identifies hidden links in Content Networks by connecting similar content nodes utilizing neural word embeddings.
3. **Event Detection**: We present an algorithm for detecting events by tracking large connected components of Content Networks over time. Our results demonstrate, that we are able to effectively identify events compared to widely used event detection techniques.


If you make use of this code, the LiCNo algorithm, or the datasets in your work, please cite the following paper:
```
@inproceedings{saravanou2017revealing,
  title={Revealing the hidden links in content networks: An application to event discovery},
  author={Saravanou, Antonia and Katakis, Ioannis and Valkanas, George and Kalogeraki, Vana and Gunopulos, Dimitrios},
  booktitle={Proceedings of the 2017 ACM on Conference on Information and Knowledge Management},
  pages={2283--2286},
  year={2017},
  organization={ACM}
 }
```


### Dataset format

The network should be stored under the `data/` folder, one file per time window. The filename should be `<time window id>.tsv`, where `<time window id>` starts from `0` to `number of time windows - 1`.

The file should be in the following format:
- One line per tweet.
- Each line should have the following *tab*-separated information: 
*tweet_id, user_id, tweet_text, timestamp, is_reply_to_tweet_id, is_reply_to_user_id*.

For example, the first few lines of a dataset can be:
```
tweet_id    user_id tweet_text  timestamp   is_reply_to_tweet_id    is_reply_to_user_id
t0	u0	the brown fox jumped over the lazy dog	1594426186		
t1	u0	brown fox cat dog	1594426189	t0	u0
t2	u1	icecream summer vacations	1594426199		
t3	u2	sea beach iced coffee	1594426206	t2	u1
```


### References 
Saravanou, A., Katakis, I., Valkanas, G., Kalogeraki, V. and Gunopulos, D., 2017, November. *Revealing the hidden links in content networks: An application to event discovery*. In Proceedings of the 2017 ACM on Conference on Information and Knowledge Management (pp. 2283-2286). 

If you make use of this code, the LiCNo algorithm, or the dataset in your work, please cite the following paper:
```
@inproceedings{saravanou2017revealing,
  title={Revealing the hidden links in content networks: An application to event discovery},
  author={Saravanou, Antonia and Katakis, Ioannis and Valkanas, George and Kalogeraki, Vana and Gunopulos, Dimitrios},
  booktitle={Proceedings of the 2017 ACM on Conference on Information and Knowledge Management},
  pages={2283--2286},
  year={2017},
  organization={ACM}
 }
```
