The Nusselt number is a dimensionless number, named after a German engineer Wilhelm Nusselt. 
the Nusselt number represents the enhancement of heat transfer through a fluid layer as a result of convection.
 Thermal Engineering (What is Nusselt Number - Definition (thermal-engineering.org))

Equations :What is Dittus-Boelter Equation - Definition (thermal-engineering.org)
 Gnielinki:What is Gnielinski Equation - Definition (thermal-engineering.org)
 https://neutrium.net/fluid-flow/hydraulic-diameter/

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