# Predictive Coding Paper Repository 
This repository provides a list of papers that are interesting or influential about Predictive Coding. If you believe I have missed any papers, please contact me at *beren@millidge.name* or make a pull request with the information about the paper. I will be happy to include it. 

## Predictive Coding 
Predictive Coding is a neurophysiologically-grounded theory of perception and learning in the brain. The core idea is that the brain always maintains a prediction of the expected state of the world, and that this prediction is then compared against the true sensory data. Where this prediction is wrong, prediction errors are generated and propagated throughout the brain. The brain's 'task' then is simply to minimize prediction errors. 
 
The key distinction of this theory is that it proposes that prediction-errors, rather than predictions, or direct representation of sense-data is in some sense the core computational primitive in the brain. 
 
Predictive coding originated in studies of ganglion cells in the retina, in light of theories in signal processing, about how it is much more efficient to send only 'different' or 'unpredicted signals' than repeating the whole signal every time -- see delta-encoding. 
 
Predictive coding has several potential neurobiologically plausible process theories proposed for it -- see 'Process Theories' section, although the empirical evidence for precise prediction error minimization in the brain is mixed 
 
Predictive coding has also been extended in several ways. It can be understood as a variational inference algorithm under a Gaussian generative model and variational distribution. It can be setup as an autoencoder (predict your input, or next-state), or else in a supervised learning fashion. 
 
Predictive coding can also be extended to a hierarchical model of multiple predictive coding layers -- as in the brain -- as well as using 'generalised coordinates' which explicitly model the higher order derivatives a state in order to be able to explicitly model dynamical systems. 
 
More recent work has also focused on the relationship between predictive coding and the backpropagation of error algorithm in machine learning where under certain assumptions, predictive coding can approximate this fundamental algorithm in a biologically plausible fashion. Although the exact details and conditions still need to be worked out. 
 
There has also been much exciting work trying to merge predictive coding with machine learning to produce highly performant predictive-coding-inspired architectures. 
 
- [Surveys and Tutorials](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#surveys-and-tutorials)
- [Classics](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#classics)
- [Neurobiological Process Theories ](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#neurobiological-process-theories-)
- [Relationship to Backpropagation](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#relationship-to-backpropagation)
- [PC-inspired machine learning](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#pc-inspired-machine-learning)
- [Extensions and Developments](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#extensions-and-developments)
- [Relationship to FEP](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#relationship-to-fep)

## Surveys and Tutorials
- [**A tutorial on the free-energy framework for modelling perception and learning**](https://www.sciencedirect.com/science/article/pii/S0022249615000759) , (2017) by *Bogacz, Rafal* [[bib]](bibtex.bib#L2-L12) 
 
 *This is a great review which introduces the basics of predictive coding and its interpretation as variational inference. It also contains sample MATLAB code that implements a simple predictive coding network. I would start here.* 
- [**The free energy principle for action and perception: A mathematical review**](https://www.sciencedirect.com/science/article/pii/S0022249617300962) , (2017) by *Buckley, Christopher L, Kim, Chang Sub, McGregor, Simon and Seth, Anil K* [[bib]](bibtex.bib#L16-L26) 
 
 *This is a fantastic review which presents a complete walkthrough of the mathematical basis of the Free Energy Principle and Variational Inference, and derives predictive coding and (continuous time and state) active inference. It also presents the 'full-construct' predictive coding including with hierarchical layers and generalised coordinates in an accessible fashion. I would reccomend reading this after Bogacz' tutorial (although be prepared -- it is a long and serious read)* 
- [**A review of predictive coding algorithms**](https://www.sciencedirect.com/science/article/pii/S027826261530035X?casa_token=zzTchZsrFesAAAAA:5bJNguAnRfn4BOjlCtmGvjiQT0Mkk3CE1By9JsrGrDIT0qY-CUKLUwVROkHB9S_kUx6mtH-nc74) , (2017) by *Spratling, Michael W* [[bib]](bibtex.bib#L29-L39) 
 
 *A short and concise review of predictive coding algorithms up to 2017.* 
- [**Predictive coding**](https://onlinelibrary.wiley.com/doi/pdf/10.1002/wcs.142?casa_token=TJvdr2nDbr8AAAAA:0T3LOAIXt6I7YYpJIqOs204qnwU0FFQiVC976sVifVv0XB4wFlrLZ7WvALY9x_qdoIGciEZWd12hfNQ) , (2011) by *Huang, Yanping and Rao, Rajesh PN* [[bib]](bibtex.bib#L42-L53) 

## Classics
- [**Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects**](https://www.nature.com/articles/nn0199_79) , (1999) by *Rao, Rajesh PN and Ballard, Dana H* [[bib]](bibtex.bib#L56-L67) 
 
 *A key influential early paper proposing predictive coding as a general theory of cortical function.* 
- [**Predictive coding: a fresh view of inhibition in the retina**](https://royalsocietypublishing.org/doi/abs/10.1098/rspb.1982.0085?casa_token=gdNrGbAlmC8AAAAA%3Ac1xArFgNym4QLB0vI-dDd0ywIS0ozVZjzjnhogf4CVpFZi2zIW8cMU3OIZwvV8cFCoVqAaDOFo_IFDY) , (1982) by *Srinivasan, Mandyam Veerambudi, Laughlin, Simon Barry and Dubs, Andreas* [[bib]](bibtex.bib#L70-L81) 
 
 *One of the earliest works proposing predictive coding in the retina.* 

## Neurobiological Process Theories 
- [**Dynamic predictive coding by the retina**](https://www.nature.com/articles/nature03689) , (2005) by *Hosoya, Toshihiko, Baccus, Stephen A and Meister, Markus* [[bib]](bibtex.bib#L84-L95) 
- [**Canonical microcircuits for predictive coding**](https://www.sciencedirect.com/science/article/pii/S0896627312009592) , (2012) by *Bastos, Andre M, Usrey, W Martin, Adams, Rick A, Mangun, George R, Fries, Pascal and Friston, Karl J* [[bib]](bibtex.bib#L96-L107) 
 
 *A key process theory paper. Proposing perhaps the default implementation of predictive coding in cortical layers.* 
- [**Predictive coding as a model of biased competition in visual attention**](https://www.sciencedirect.com/science/article/pii/S0042698908001466) , (2008) by *Spratling, Michael W* [[bib]](bibtex.bib#L109-L120) 
 
 *Demonstrates that predictive coding is equivalent to popular biased competition models of neural function.* 
- [**Reconciling predictive coding and biased competition models of cortical function**](https://www.frontiersin.org/articles/10.3389/neuro.10.004.2008/full) , (2008) by *Spratling, Michael W* [[bib]](bibtex.bib#L134-L144) 

 
## Contributing 
 
To contribute, please make pull requests adding entries to the bibtex file.  
 
 The README file was generated from bibtex using the `bibtex_to_md.py` file. 
 The keywords to use for each classification ('Classic','Backprop') can be found at the bottom of the .py file. 

 
*This code and structure is heavily inspired by https://github.com/optimass/continual_learning_papers.*