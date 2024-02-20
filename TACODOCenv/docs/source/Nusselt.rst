The Nusselt Number is a dimensionaless number that represents the temperature gradient and the heat transfer convection at the surface of the fluid. 
TACOCAT will calculate the Nusselt Number by using the information that is provided is needed.
The user will specify which geometry they will be working with. Currently, TACOCAT uses two different Nusselt Number correlations.
The first is the Dittus-Boelter Equation. This correlation is used when the fluid expereiences a large tempurature difference across it during a fully developed turbulent flow in small circular tubes.
It should be used when calculating the Nusselt Number for smooth tubes. 
This correlation uses the hydraulic diameter, the Reynolds number, the Prandtl number, and the Nusselt number.
For the Dittus-Boelter correlation, the Prandtl number should range 0.6 <=Pr<= 160.
The Reynolds number shoud be greater than 10000 (ReDₕ > 10000).  
It is dependent on the hydraulic diameter of the pipe.
The hydraulic diameter is used when a circular pipe is connected to a non-circular pipe. 
The hydraulic diameter should not be used for a laminar flow because the fluid is governed by the geometry of the pipe.
Because of this, the hydraulic diameter should be used with turbulent flow systems because the geometry of the fluid is not as important.
This also means that the Dittus-Boelter correlation should only be used for a turbulent flow system.

The Dittus-Boelter correlation is given as:
.. math::

    Nu=0.23ReDₕ^{0.8} Pr^{0.4} 

The next Nusselt Number correlation that is implemented in TACOCAT is the Gnielinski correlation. This correlation is more intricate than the Dittus-Boelter correlation. 
The Gnielinski correlation should be used to authentivate tubes that expereiences a large Reynolds number range. This correlation also covers pipe transitional areas.
In order to use the Gnielinski correlation, the Reynolds Number ranges between 3000 <=ReDₕ<= 5*10⁶. The Prandtl number ranges from 0.5 <= Pr <= 2000.
This particular Nusselt number correlation uses the Darcy friction factor (f). It is a dimensionaless quantity that is used to represent the frictional losses in pipes or in ducts. It can also be used in open-flow channels
The friction factor is dependent on the Reynolds number for the fluid's flow and to understand the amount of roughness that a pipe's inner surface expereiences. 
The Darcy friction factor can be used for both laminar and turbulent flows. For laminar flow, the friction factor is independent of the roughness at the inner surface of a pipe. 
For Turbulent flow, the friction factor is highly depended on the realtive roughness. It will be independent of the Reynolds number if the Reynolds number becomes very large.

The Gnielinski correlation is given as:
.. math::
    
    NuDₕ = \frac{(\frac{f}{8})(ReDₕ-1000)Pr}/{1+12.7((\frac{f}/{8})^{1/2}(Pr^{2/3}-1))}



References:

Equations :What is Dittus-Boelter Equation - Definition (thermal-engineering.org)
 Gnielinki:What is Gnielinski Equation - Definition (thermal-engineering.org)
 https://neutrium.net/fluid-flow/hydraulic-diameter/
 https://www.nuclear-power.com/nuclear-engineering/fluid-dynamics/major-head-loss-friction-loss/darcy-friction-factor-2/