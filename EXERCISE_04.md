# 完成作业1.5
 Consider again a decay problem with two types of nuclei of type A into ones of type B, while nuclei of type B, while nuclei of type
B decay into ones of type A. Strictly speaking, this is not a "decay" process,since it is possible for the type B nuclei to turn back
into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and
B which have equal energies. The corresponding rate equations are <br/>
<img src="http://latex.codecogs.com/gif.latex?\frac{dN_A}{dt}=\frac{N_B}{\tau}-\frac{N_A}{\tau}" alt="" title="" /> <br/>
<img src="http://latex.codecogs.com/gif.latex?\frac{dN_B}{dt}=\frac{N_A}{\tau}-\frac{N_B}{\tau}" alt="" title="" /> <br/>
where for simplicity we have assumed that the two types of decay are characterized by the same time constant,τ. Solve this system of 
equatiions for the numbers of nuclei, NA=100, NB=0, etc., and take τ=1s. Show that your numercial results are consistent with the idea
that the system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt
should vanish.

# 方程的解析
## 假设原子的衰变方程
### <img src="http://latex.codecogs.com/gif.latex?\frac{dN}{dt}=-\frac{N}{\tau}" alt="" title="" />
对N做泰勒展开得到 <br/>
  ![](http://latex.codecogs.com/gif.latex?N%28%5CDelta%29%3DN%280%29&plus;%5Cfrac%7BdN%7D%7Bdt%7D%5Ccdot%5CDelta%20t&plus;%5Cfrac%7B1%7D%7B2%7D%5Ccdot%5Cfrac%7Bd%5E2%20N%7D%7Bdt%5E2%7D&plus;...)
