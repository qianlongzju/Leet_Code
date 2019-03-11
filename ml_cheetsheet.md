



1. hinge loss

2. sigmoid

   1. \-  Squashes numbers to range [0,1] 
   2. \-  Historically popular since they have nice interpretation as a saturating “firing rate” of a neuron 
   3. problems
      1. Saturated neurons “kill” the gradients 
      2. Sigmoid outputs are not zero-centered 
      3. exp() is a bit compute expensive 

3. tanh

   1. \-  Squashes numbers to range [-1,1] 
   2. \-  zero centered (nice) 
   3. \-  still kills gradients when saturated :( 

4. relu

   1. \-  Does not saturate (in +region) 
   2. \-  Very computationally efficient 
   3. Converges much faster than sigmoid/tanh in practice (e.g. 6x) 
   4. Actually more biologically plausible than sigmoid
   5. Not zero-centered output 
   6. An annoyance: 

5. leaky Relu max(0.01x, x)

   1. will not “die”. 

6. pRelu

7. ELU(Exponential Linear Units)     alpha*(exp(x)-1) if x <= 0

8. ![image-20180805160420219](/Users/isaiah/Workspace/LeetCode/imgs/image-20180805160420219.png)

9. zero mean data -> when the input to a neuron is always positive:

10. the gradients on w always all positive or all negative(zig zag path for update w)

11. ![image-20180805161020190](/Users/isaiah/Workspace/LeetCode/imgs/image-20180805161020190.png)

12. BN:Usually inserted after Fully Connected or Convolutional layers, and before nonlinearity. 

13. ![image-20180805161620625](/Users/isaiah/Workspace/LeetCode/imgs/image-20180805161620625.png)

14. loss not going down: 

    learning rate too low 

    loss exploding: 

    learning rate too high 

15. 

    1.  Adam is a good default choice in most cases 
    2. If you can afford to do full batch updates then try out L-BFGS (and don’t forget to disable all sources of noise) 

    

    16. winograd transformation   -> conv 




