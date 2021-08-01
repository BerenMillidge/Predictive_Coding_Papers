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
- [Neuroscience applications](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#neuroscience-applications)
- [Relationship to Backpropagation](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#relationship-to-backpropagation)
- [PC-inspired machine learning](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#pc-inspired-machine-learning)
- [Extensions and Developments](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#extensions-and-developments)
- [Relationship to FEP](https://github.com/BerenMillidge/Predictive_Coding_Papers/blob/master/README.md#relationship-to-fep)

## Surveys and Tutorials
- [**A tutorial on the free-energy framework for modelling perception and learning**](https://www.sciencedirect.com/science/article/pii/S0022249615000759) , (2017) by *Bogacz, Rafal* [[bib]](bibtex.bib#L2-L12) 
 
 *This is a great review which introduces the basics of predictive coding and its interpretation as variational inference. It also contains sample MATLAB code that implements a simple predictive coding network. I would start here.* 
- [**Predictive Coding: a Theoretical and Experimental Review**](https://arxiv.org/pdf/2107.12979.pdf) , (2021) by *Millidge, Beren, Seth, Anil and Buckley, Christopher L* [[bib]](bibtex.bib#L24-L31) 
 
 *This review walks through the mathematical framework and potential neural implementations in predictive coding, and also covers much recent work on the relationship between predictive coding and machine learning.* 
- [**The free energy principle for action and perception: A mathematical review**](https://www.sciencedirect.com/science/article/pii/S0022249617300962) , (2017) by *Buckley, Christopher L, Kim, Chang Sub, McGregor, Simon and Seth, Anil K* [[bib]](bibtex.bib#L85-L95) 
 
 *This is a fantastic review which presents a complete walkthrough of the mathematical basis of the Free Energy Principle and Variational Inference, and derives predictive coding and (continuous time and state) active inference. It also presents the 'full-construct' predictive coding including with hierarchical layers and generalised coordinates in an accessible fashion. I would reccomend reading this after Bogacz' tutorial (although be prepared -- it is a long and serious read)* 
- [**A review of predictive coding algorithms**](https://www.sciencedirect.com/science/article/pii/S027826261530035X?casa_token=zzTchZsrFesAAAAA:5bJNguAnRfn4BOjlCtmGvjiQT0Mkk3CE1By9JsrGrDIT0qY-CUKLUwVROkHB9S_kUx6mtH-nc74) , (2017) by *Spratling, Michael W* [[bib]](bibtex.bib#L98-L108) 
 
 *A short and concise review of predictive coding algorithms up to 2017.* 
- [**Predictive coding**](https://onlinelibrary.wiley.com/doi/pdf/10.1002/wcs.142?casa_token=TJvdr2nDbr8AAAAA:0T3LOAIXt6I7YYpJIqOs204qnwU0FFQiVC976sVifVv0XB4wFlrLZ7WvALY9x_qdoIGciEZWd12hfNQ) , (2011) by *Huang, Yanping and Rao, Rajesh PN* [[bib]](bibtex.bib#L111-L122) 
 
 *A nice review of simple predictive coding architectures with a focus on their potential implementation in the brain.* 

## Classics
- [**Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects**](https://www.nature.com/articles/nn0199_79) , (1999) by *Rao, Rajesh PN and Ballard, Dana H* [[bib]](bibtex.bib#L125-L136) 
 
 *A key influential early paper proposing predictive coding as a general theory of cortical function.* 
- [**Predictive coding: a fresh view of inhibition in the retina**](https://royalsocietypublishing.org/doi/abs/10.1098/rspb.1982.0085?casa_token=gdNrGbAlmC8AAAAA%3Ac1xArFgNym4QLB0vI-dDd0ywIS0ozVZjzjnhogf4CVpFZi2zIW8cMU3OIZwvV8cFCoVqAaDOFo_IFDY) , (1982) by *Srinivasan, Mandyam Veerambudi, Laughlin, Simon Barry and Dubs, Andreas* [[bib]](bibtex.bib#L139-L150) 
 
 *One of the earliest works proposing predictive coding in the retina.* 
- [**A theory of cortical responses**](https://royalsocietypublishing.org/doi/abs/10.1098/rstb.2005.1622?casa_token=9zU-Epc4Iw4AAAAA%3AmYQq9buUvH2tb1xtL8VXFp0oHtJVGZ_4MSymueoSBUreJAhsqEOB3D-fXJnSqMnbTYP3VBo0BxwHWYE) , (2005) by *Friston, Karl* [[bib]](bibtex.bib#L226-L237) 
 
 *An early but complete description of predictive coding as an application of the FEP and variational inference under Gaussian and Laplace assumptions. Also surprisingly readable. This is core reading on predictive coding and the FEP* 
- [**Learning and inference in the brain**](https://www.sciencedirect.com/science/article/pii/S0893608003002454?casa_token=Z-HR_To6rxwAAAAA:88ducipot59VHoRHJu1Ej6Kz5oLn-RMooUV9rR1fnkH50D5aNvLNENIF2XBa_3tZ0izMX5U2ED8) , (2003) by *Friston, Karl* [[bib]](bibtex.bib#L239-L250) 
 
 *The first paper establishing the links between predictive coding and variational inference.* 
- [**Attention, uncertainty, and free-energy**](https://www.frontiersin.org/articles/10.3389/fnhum.2010.00215/full) , (2010) by *Feldman, Harriet and Friston, Karl* [[bib]](bibtex.bib#L253-L263) 
 
 *Makes a conjectured link between precision in predictive coding and attention in the brain.* 
- [**Hierarchical models in the brain**](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000211) , (2008) by *Friston, Karl* [[bib]](bibtex.bib#L265-L276) 
 
 *Presents the 'full-construct' predictive coding model with both hierarchies and generalised coordinates.* 
- [**DEM: a variational treatment of dynamic systems**](https://www.sciencedirect.com/science/article/pii/S1053811908001894?casa_token=RBtljR9mpKMAAAAA:EAAQB59MLINQl8q4it_Pxnz6EbRaqvO0mMey40hdf29Qy0kKkH69qWN24jnmhcOXamuXWBqFAG4) , (2008) by *Friston, Karl J, Trujillo-Barreto, N and Daunizeau, Jean* [[bib]](bibtex.bib#L278-L289) 
 
 *Extends predictive coding to generalised coordinates, and derives the necessary inference algorithms for working with them -- i.e. DEM, dynamic expectation maximisation.* 
- [**Generalised filtering**](https://www.hindawi.com/journals/mpe/2010/621670/) , (2010) by *Friston, Karl, Stephan, Klaas, Li, Baojuan and Daunizeau, Jean* [[bib]](bibtex.bib#L291-L300) 
- [**Variational filtering**](https://www.sciencedirect.com/science/article/pii/S1053811908002462?casa_token=bzK7h_aIzY0AAAAA:rg1CzE6vNo-cktIHO_9EAoqmR5Zpy89klEn-Wy3NAzMoR8NcWgaF5_zEzyhrRB76N5RPyCZTIlY) , (2008) by *Friston, Karl J* [[bib]](bibtex.bib#L303-L314) 
 
 *Foundational treatment of variational inference for dynamical systems, as represented in generalised coordinates. Also relates variational filtering to other non-variational schemes like particle filtering and Kalman filtering.* 
- [**Surfing uncertainty: Prediction, action, and the embodied mind**](https://books.google.co.uk/books?hl=en&lr=&id=TnqECgAAQBAJ&oi=fnd&pg=PP1&dq=andy+clark+surfing+uncertainty&ots=aurm6iDbJR&sig=A5uoJIteAk4JDCEpnQaa2KAbfg4&redir_esc=y#v=onepage&q=andy%20clark%20surfing%20uncertainty&f=false) , (2015) by *Clark, Andy* [[bib]](bibtex.bib#L409-L416) 
 
 *Andy's book is great for a high level overview, strong intuition pumps for understanding the theory, and a fantastic review of potential evidence and neuropyschiatric applications.* 

## Neurobiological Process Theories 
- [**Dynamic predictive coding by the retina**](https://www.nature.com/articles/nature03689) , (2005) by *Hosoya, Toshihiko, Baccus, Stephen A and Meister, Markus* [[bib]](bibtex.bib#L153-L164) 
- [**Canonical microcircuits for predictive coding**](https://www.sciencedirect.com/science/article/pii/S0896627312009592) , (2012) by *Bastos, Andre M, Usrey, W Martin, Adams, Rick A, Mangun, George R, Fries, Pascal and Friston, Karl J* [[bib]](bibtex.bib#L165-L176) 
 
 *A key process theory paper. Proposing perhaps the default implementation of predictive coding in cortical layers.* 
- [**Predictive coding as a model of biased competition in visual attention**](https://www.sciencedirect.com/science/article/pii/S0042698908001466) , (2008) by *Spratling, Michael W* [[bib]](bibtex.bib#L178-L189) 
 
 *Demonstrates that predictive coding is equivalent to popular biased competition models of neural function.* 
- [**Dopamine role in learning and action inference**](https://elifesciences.org/articles/53262.pdf) , (2020) by *Bogacz, Rafal* [[bib]](bibtex.bib#L190-L200) 
- [**Reconciling predictive coding and biased competition models of cortical function**](https://www.frontiersin.org/articles/10.3389/neuro.10.004.2008/full) , (2008) by *Spratling, Michael W* [[bib]](bibtex.bib#L215-L225) 
- [**Neural elements for predictive coding**](https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01792/full) , (2016) by *Shipp, Stewart* [[bib]](bibtex.bib#L315-L325) 
 
 *Another great overview of a potentially neurobiologiclaly plausible process theory for predictive coding.* 
- [**Reflections on agranular architecture: predictive coding in the motor cortex**](https://www.sciencedirect.com/science/article/pii/S0166223613001604) , (2013) by *Shipp, Stewart, Adams, Rick A and Friston, Karl J* [[bib]](bibtex.bib#L327-L338) 
 
 *A process theory of predictive coding including action predictions which implement active inference (continuous version).* 
- [**Cerebral hierarchies: predictive processing, precision and the pulvinar**](https://royalsocietypublishing.org/doi/full/10.1098/rstb.2014.0169) , (2015) by *Kanai, Ryota, Komura, Yutaka, Shipp, Stewart and Friston, Karl* [[bib]](bibtex.bib#L341-L352) 
- [**Great expectations: is there evidence for predictive coding in auditory cortex?**](https://www.sciencedirect.com/science/article/pii/S030645221730547X) , (2018) by *Heilbron, Micha and Chait, Maria* [[bib]](bibtex.bib#L353-L363) 
- [**Predictive coding in sensory cortex**](https://link.springer.com/chapter/10.1007/978-1-4939-2236-9_11) , (2015) by *Kok, Peter and de Lange, Floris P* [[bib]](bibtex.bib#L364-L373) 
- [**Evaluating the neurophysiological evidence for predictive processing as a model of perception**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7187369/) , (2020) by *Walsh, Kevin S, McGovern, David P, Clark, Andy and O'Connell, Redmond G* [[bib]](bibtex.bib#L580-L591) 
 
 *A great review delving deep into the evidence for predictive coding being implemented in the brain. Evidence is currently somewhat lacking, although the flexibility of the predictive coding framework allows it to encompass a lot of the findings here.* 
- [**Fitting predictive coding to the neurophysiological data**](https://www.sciencedirect.com/science/article/pii/S0006899319303592?casa_token=Mq4I-lQm6OMAAAAA:qGWBzjDg799T4lW-YLpp6Mm6Hkh5WhNO1D4teQVE6fRuRCY_2Uv3q2d3xpgXtFCzdhzBy9mzSjg) , (2019) by *Spratling, MW* [[bib]](bibtex.bib#L652-L662) 
- [**Predictive processing: a canonical cortical computation**](https://www.sciencedirect.com/science/article/pii/S0896627318308572) , (2018) by *Keller, Georg B and Mrsic-Flogel, Thomas D* [[bib]](bibtex.bib#L663-L674) 

## Neuroscience applications
- [**Predictive coding is a consequence of energy efficiency in recurrent neural networks**](https://www.biorxiv.org/content/10.1101/2021.02.16.430904v1.abstract) , (2021) by *Ali, Abdullahi, Ahmad, Nasir, de Groot, Elgar, van Gerven, Marcel AJ and Kietzmann, Tim C* [[bib]](bibtex.bib#L75-L83) 
- [**The predictive coding account of psychosis**](https://www.sciencedirect.com/science/article/pii/S0006322318315324) , (2018) by *Sterzer, Philipp, Adams, Rick A, Fletcher, Paul, Frith, Chris, Lawrie, Stephen M, Muckli, Lars, Petrovic, Predrag, Uhlhaas, Peter, Voss, Martin and Corlett, Philip R* [[bib]](bibtex.bib#L375-L386) 
- [**An interoceptive predictive coding model of conscious presence**](https://www.frontiersin.org/articles/10.3389/fpsyg.2011.00395/full) , (2012) by *Seth, Anil K, Suzuki, Keisuke and Critchley, Hugo D* [[bib]](bibtex.bib#L387-L397) 
- [**Extending predictive processing to the body: emotion as interoceptive inference**](https://pdfs.semanticscholar.org/d8ab/0cbc439db9c0a5783bc4c51a7bb6454ff711.pdf) , (2013) by *Seth, Anil K and Critchley, Hugo D* [[bib]](bibtex.bib#L398-L408) 
- [**An aberrant precision account of autism**](https://www.frontiersin.org/articles/10.3389/fnhum.2014.00302/full) , (2014) by *Lawson, Rebecca P, Rees, Geraint and Friston, Karl J* [[bib]](bibtex.bib#L594-L604) 
- [**A predictive coding perspective on autism spectrum disorders**](https://www.frontiersin.org/articles/10.3389/fpsyg.2013.00019/full) , (2013) by *Van Boxtel, Jeroen JA and Lu, Hongjing* [[bib]](bibtex.bib#L605-L615) 
- [**Predictive coding: an account of the mirror neuron system**](https://pubmed.ncbi.nlm.nih.gov/17429704/) , (2007) by *Kilner, James M, Friston, Karl J and Frith, Chris D* [[bib]](bibtex.bib#L616-L627) 
- [**Predictive coding as a model of response properties in cortical area V1**](https://www.jneurosci.org/content/30/9/3531.short) , (2010) by *Spratling, Michael W* [[bib]](bibtex.bib#L628-L639) 
- [**Predictive coding explains binocular rivalry: An epistemological review**](https://www.sciencedirect.com/science/article/pii/S0010027708001327?casa_token=kCwdW4Cxnm0AAAAA:wLNw7Ba9dhTAU4Lb8lhTlzHz32HO3lKVznlWLY5wLgVzJzKRYY-QkZfZtp_KmvhZi5kWddOQxg4) , (2008) by *Hohwy, Jakob, Roepstorff, Andreas and Friston, Karl* [[bib]](bibtex.bib#L640-L651) 

## Relationship to Backpropagation
- [**An approximation of the error backpropagation algorithm in a predictive coding network with local hebbian synaptic plasticity**](https://www.mitpressjournals.org/doi/full/10.1162/NECO_a_00949) , (2017) by *Whittington, James CR and Bogacz, Rafal* [[bib]](bibtex.bib#L419-L430) 
- [**Predictive Coding Approximates Backprop along Arbitrary Computation Graphs**](https://arxiv.org/abs/2006.04182) , (2020) by *Millidge, Beren, Tschantz, Alexander and Buckley, Christopher L* [[bib]](bibtex.bib#L431-L438) 
- [**Can the Brain Do Backpropagation?---Exact Implementation of Backpropagation in Predictive Coding Networks**](https://proceedings.neurips.cc/paper/2020/hash/fec87a37cdeec1c6ecf8181c0aa2d3bf-Abstract.html) , (2020) by *Song, Yuhang, Lukasiewicz, Thomas, Xu, Zhenghua and Bogacz, Rafal* [[bib]](bibtex.bib#L440-L448) 
- [**Predictive Coding Can Do Exact Backpropagation on Convolutional and Recurrent Neural Networks**](https://arxiv.org/abs/2103.03725) , (2021) by *Salvatori, Tommaso, Song, Yuhang, Lukasiewicz, Thomas, Bogacz, Rafal and Xu, Zhenghua* [[bib]](bibtex.bib#L450-L457) 

## PC-inspired machine learning
- [**Representation learning with contrastive predictive coding**](https://arxiv.org/pdf/1807.03748.pdf) , (2018) by *Oord, Aaron van den, Li, Yazhe and Vinyals, Oriol* [[bib]](bibtex.bib#L15-L22) 
- [**Continual learning of recurrent neural networks by locally aligning distributed representations**](https://ieeexplore.ieee.org/document/8963851) , (2020) by *Ororbia, Alexander, Mali, Ankur, Giles, C Lee and Kifer, Daniel* [[bib]](bibtex.bib#L34-L45) 
- [**The neural coding framework for learning generative models**](https://arxiv.org/pdf/2012.03405.pdf) , (2020) by *Ororbia, Alexander and Kifer, Daniel* [[bib]](bibtex.bib#L46-L53) 
- [**Backprop-Free Reinforcement Learning with Active Neural Generative Coding**](https://arxiv.org/pdf/2107.07046.pdf) , (2021) by *Ororbia, Alexander and Mali, Ankur* [[bib]](bibtex.bib#L54-L61) 
- [**Spiking Neural Predictive Coding for Continual Learning from Data Streams**](https://arxiv.org/pdf/1908.08655.pdf) , (2019) by *Ororbia, Alexander* [[bib]](bibtex.bib#L63-L70) 
- [**Deep predictive coding networks for video prediction and unsupervised learning**](https://arxiv.org/abs/1605.08104) , (2016) by *Lotter, William, Kreiman, Gabriel and Cox, David* [[bib]](bibtex.bib#L512-L519) 
- [**Video representation learning by dense predictive coding**](https://openaccess.thecvf.com/content_ICCVW_2019/html/HVU/Han_Video_Representation_Learning_by_Dense_Predictive_Coding_ICCVW_2019_paper.html) , (2019) by *Han, Tengda, Xie, Weidi and Zisserman, Andrew* [[bib]](bibtex.bib#L520-L528) 
- [**Deep predictive coding network for object recognition**](https://arxiv.org/abs/1802.04762) , (2018) by *Wen, Haiguang, Han, Kuan, Shi, Junxing, Zhang, Yizhen, Culurciello, Eugenio and Liu, Zhongming* [[bib]](bibtex.bib#L529-L536) 
- [**Deep predictive coding networks**](https://arxiv.org/abs/1301.3541) , (2013) by *Chalasani, Rakesh and Principe, Jose C* [[bib]](bibtex.bib#L537-L544) 
- [**Deep predictive coding network with local recurrent processing for object recognition**](https://arxiv.org/pdf/1802.04762.pdf) , (2018) by *Han, Kuan, Wen, Haiguang, Zhang, Yizhen, Fu, Di, Culurciello, Eugenio and Liu, Zhongming* [[bib]](bibtex.bib#L545-L554) 
- [**Meaningful representations emerge from sparse deep predictive coding**](https://www.researchgate.net/profile/Laurent_Perrinet/publication/331246369_Meaningful_representations_emerge_from_Sparse_Deep_Predictive_Coding/links/5cbe0d1ba6fdcc1d49a86405/Meaningful-representations-emerge-from-Sparse-Deep-Predictive-Coding.pdf) , (2019) by *Boutin, Victor, Franciosini, Angelo, Ruffier, Franck and Perrinet, Laurent* [[bib]](bibtex.bib#L555-L562) 
- [**Hierarchical Predictive Coding Models in a Deep-Learning Framework**](https://arxiv.org/abs/2005.03230) , (2020) by *Hosseini, Matin and Maida, Anthony* [[bib]](bibtex.bib#L563-L570) 
- [**PredNet and Predictive Coding: A Critical Review**](https://dl.acm.org/doi/pdf/10.1145/3372278.3390694?casa_token=-IdjNoI837MAAAAA:XUBgc0lCY-iximHZdHy2lmspktIwT62dW9fYn4UzFyvA2O1JJFtTlCC2e_mKJaEr6nsYNacjnOJ_Rg) , (2020) by *Rane, Roshan Prakash, Sz{\"u}gyi, Edit, Saxena, Vageesh, Ofner, Andr{\'e} and Stober, Sebastian* [[bib]](bibtex.bib#L571-L579) 

## Extensions and Developments
- [**Relaxing the constraints on predictive coding models**](https://arxiv.org/abs/2010.01047) , (2020) by *Millidge, Beren, Tschantz, Alexander, Seth, Anil and Buckley, Christopher L* [[bib]](bibtex.bib#L459-L466) 
 
 *This paper investigates how serveral biologically implausible aspects of the standard predictive coding algorithm -- namely requiring symmetric forward and backward weights, nonlinear derivatives, and 1-1 error unit connections can be relaxed without unduly harming performance of the network.* 
- [**Making Predictive Coding Networks Generative**](https://arxiv.org/abs/1910.12151) , (2019) by *Orchard, Jeff and Sun, Wei* [[bib]](bibtex.bib#L469-L476) 
- [**Tightening the Biological Constraints on Gradient-Based Predictive Coding**](https://arxiv.org/pdf/2104.15137.pdf) , (2021) by *Alonso, Nick and Neftci, Emre* [[bib]](bibtex.bib#L478-L485) 
 
 *This paper further looks at how various implausibility of the predictive coding algorithm can be relaxed, and focuses especially on the question of how negative prediction errors could be represented, as well as invents a divisive prediction error scheme -- where prediction errors are the activities divided by the predictions.* 
- [**A Predictive-Coding Network That Is Both Discriminative and Generative**](https://www.mitpressjournals.org/doi/abs/10.1162/neco_a_01311) , (2020) by *Sun, Wei and Orchard, Jeff* [[bib]](bibtex.bib#L489-L500) 
- [**Dopamine role in learning and action inference**](https://elifesciences.org/articles/53262) , (2020) by *Bogacz, Rafal* [[bib]](bibtex.bib#L190-L200) 

 
## Contributing 
 
To contribute, please make pull requests adding entries to the bibtex file.  
 
 The README file was generated from bibtex using the `bibtex_to_md.py` file. 
 The keywords to use for each classification ('Classic','Backprop') can be found at the bottom of the .py file. 

 
*This code and structure is heavily inspired by https://github.com/optimass/continual_learning_papers.*