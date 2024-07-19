---
aliases:
---
> MC
> In this video I'm going to teach you everything I learned in an undergrad physics class in X minutes.

# Chapter 1: Electrostatics

## Coulomb's Law

BLENDER ATOM ANIMATION

Camera zooms into BOHR ATOM

> MC
> This is an atom. In the center are protons with positive charge and the neutrons with neutral charge. And on the outside are electrons with negative charge.

Camera shifts to TWO PROTONS

> MC
> Like charges repel each other.

Camera shifts to PROTON AND ELECTRON

> MC
> And opposite charges attract.

Camera darkens

> MC
> What we want to be able to determine is how much they attract or repel each other, but there's a problem with that.



INT. HOUSE BASEMENT WALL -- DAY

> MC
> In reality you don't just have free charges floating around in space. And so instead you have to measure the force on charges like this-

MC holds up WHITEBOARD, showing an object with more positive charges than negatives, and and object with more negative charges than positive.

> MC
> So you can see that one object has more positive charges than negative, which means that in total, it's going to have a slight positive charge. The other object has more negative charges than positive, so it's going to have a slight negative charge. Now we have a slight positive charge on one object, and a slight negative charge on the other, which means that these two objects will attract each other.



EXT. BUSHES/FLOWERS -- DAY

MC holds glass cylinder and cloth

> MC
> What we can do is take an object like glass, and (MC rubs glass with cloth) rub it with something like this cloth. And what happens is the electrons from the glass get removed and moved over to the glass, leaving the glass with more protons than electrons, which means it has a positive charge. If you get two charged objects this way, you can measure the force between them. If you do that, you'll find that-


MANIM 2D

Proportionality laws are written, two example charges are shown above them, labeled "q_1" and "q_2."

> MC
> The force between two charged objects is proportional to the charge on each of those objects. So if I double the charge on one of the objects, the force between them doubles. If I double the charge on the other object, the force also doubles. If I triple the charge, the force triples. q1 is the charge on object 1, and q2 is the charge on object 2. The force is also inversely proportional to the radius squared. If I make the charges twice as far apart, the force goes down by a factor of 4. If I make them 10 times further apart, the force decreases 100 times.
> 
> If you combine all these, what you get is the electric force is equal to some constant, times charge 1, times charge 2, divided by the radius squared. This is Coulomb's Law.
> 
> And you might notice that it looks very similar to gravity. In fact, if you compare Coulomb's Law with the gravity equation, they're nearly identical, except with gravity you have the masses instead of the charges, and also the constants are a lot different. The electric force is over 100 quintillion times stronger than the gravitational force.

## Electric Field

INT. HOUSE BASEMENT WALL -- DAY

MC Holds two spherical objects representing charges.

> MC
> So that's how things would work if you had two charged objects, attracting or repelling each other, but what if you only had one charge?

MANIM 2D

> MC
> So let's imagine we have a positive charge, and then we pick some point out in space and we say "hey, what would happen if I put another charge here?" We already know the magnitude of the force, k q1 q2 over r-squared, and we also know that they're either gonna attract or repel. So what we can do is we can get the unit vector -- vector with length one -- that points between them, called r-hat, to get the direction of the force. And notice that if the charges have opposite signs, then we'll get a negative in our equation, so the r-hat will point in the other direction. This makes sense because opposite charges should attract each other.
> 
> If we set the charge at this point equal to positive one, then one of the charges will end up dropping out of the equation, and what we're left with is the electric field, which is equal to some constant, times the source charge, divided by the radius squared. The electric field basically tells us what kind of force we're going to get if we put a positive one charge at any point.
> 
> We can pick one point in space and find the electric field, so it looks something like this. Or, we can show the electric field everywhere. You can see that if I put a positive charge somewhere near this one, it's going to flow away, because positive charges repel each other.
> 
> You can do the same thing with a negative charge. So now all of the arrows point toward the center, because our plus-one charge would want to attract to the negative in the center.
> 
> Or, you could put a negative and a positive together, and in that case you can calculate the electric field at each point by just adding up the individual electric field from the negative charge and the positive charge. Here you can see that the arrows flow away from the positive charge and towards the negative, which makes sense because our plus-one charge would repel the positive and attract the negative.

==INT. HOUSE BASEMENT WALL -- DAY==

> MC
> So if you want to calculate the electric field from some continuous object, all you have to do is break it into a bunch of very tiny charges, and add up the electric field from each charge.

MANIM

> For example, if I have a continuous line of charges, then I can break it up into many tiny pieces, and calculate the electric field from each piece.
> 
> The way you do that is by doing k q over r-squared, just like normal, except our q is infinitesimally small, a differential charge, dq. But what exactly is dQ equal to? Well if we know the total charge on the entire line, and the length of that line, then we can get the charge density as the charge over the length, now if we multiply that by some length, the lengths cancel and we end up with charge again. So we can say that our differential charge is equal to the charge density times a very tiny length, dx. And now if we add up these tiny charges with an integral, we can calculate the electric field at some point from this line. And if you want to do it for some other object, you just need to find another way to break it into tiny charges like this.
> 
> So if you wanted to solve this integral you would pick a point for the electric field like this point, P. We can then find the radius with the Pythagorean theorem and also the r-hat vector, and then we have something we can solve.
> 
> And the only problem with this is that, sometimes, it's really difficult to calculate. I mean, would you want to solve that? Luckily there's a much easier way to solve this, and to do it we have to talk about flux.

## Electric Flux

MANIM 2D

Vector field and a net

> MC
> Let's say I have a vector field that represents the wind, and I want to catch the wind with a net. How can I create a way to measure how much wind is caught by the net?
> 
> Well if the wind is blowing stronger, then I'll probably catch more, and also if the net is bigger I'll catch more. And also if the net points perpendicular to the wind, then I'll get more.
> 
> In order to describe this, we'll need to use the net's area vector, which is just a vector perpendicular to the net with a length equal to the net's area. So if the net has a length of 5, this vector also has a length of 5.
> 
> If either the wind is bigger, the net's area vector is bigger, or they point more in the same direction, then we'll catch more wind, which means we can write our ability to catch wind as the dot product of the wind and the area vectors.
> 
> And this is exactly what flux is, it's just how much some vector field flows through a given area. If you have a more complicated surface, then you just need to break it up into several tiny areas, dAs, and add up the flux across the whole surface (integral of **F** dot d**A**). The electric flux is just how much electric field flows through some area.

## Gauss's Law

MANIM 3D ANIMATION

> MC
> So to calculate electric flux, we'll start with a charge, and we'll surround it with a sphere like this. To make things easier to see, we'll draw them in two dimensions, but, remember that we're really making a case for three dimensions here.

MANIM 2D ANIMATION

> MC
> We've already seen the electric field for a positive charge. It points outward because it repels a hypothetical plus-one charge in the vicinity. Our goal is to find the electric flux through the sphere. To do that we'll first restrict our view to the electric field specifically on the surface of this sphere. We can also see the differential area vectors, which each point perpendicular to the surface.
> 
> Writing out the flux equation, we get this, where the circle just means we're adding up over a closed surface. Since both the electric field and the area vectors always point away from the charge, in the same direction, we can simplify this from the dot product of the two vectors to simply multiplying the magnitudes of each of the vectors.
> 
> Recall that the electric field equation is a function of radius. Since a sphere is at constant radius, the electric field is constant across our entire integration, so we can pull it out of the integral.
> 
> Looking at our simplified integral, we see that we're integrating little pieces of the surface area, across the entire surface. So this whole integral simplifies to just the area of the surface.
>
> And now we can plug things in. kq over r-squared for the electric field, and 4 pi r-squared, the surface area of a sphere, for our sphere. The radius squared cancels in each case, and we're left with a bunch of constants, as well as the charge. We'll go ahead and rewrite these constants as 1 over epsilon-naught.
> 
> And this equation right here is gauss's law. The electric flux is equal to the charge inside the surface, divided by epsilon naught. And the thing that makes this powerful is that it applies for any closed surface, usually called a "Gaussian Surface," instead of just a sphere.
> 
> To see why, we can draw a completely general surface around this sphere. The only constraint of this surface is that it must be closed. Now we'll extend two line segments from the charge to each of the surfaces. We'll call the area enclosed by the sphere A1 and the area enclosed by our general surface A2. The radius to the sphere is called r and the radius to the general surface is some scaling factor n multiplied by r.
> 
> As we've seen before, we'll write the dot product in its cosine form. So the electric flux through the second area is equal to the electric field at the second area, times the cosine of theta, times some small area2, added up across the surface. The angle theta points between the electric field and the area vector, so it's this angle right here.
> 
> The component of A2 that's perpendicular to the electric field lines looks like this. And in fact it's the same as A2 times the cosine of theta. To see why, consider if theta is zero. The cosine will end up going away, so we just get electric field times the area, and the perpendicular area and a2 are the same. If theta is a right angle, then there's no perpendicular area, and there's also no flux, because the cosine gives us a zero.
> 
> So we can rewrite the flux integral as the accumulation of the electric field E2 times some differential perpendicular area.
> 
> Now remember that the electric field is some constant, times the charge, divided by the radius squared. So if we increase the radius to n times r, then we introduce a 1 over n-squared into the expression. This means that E2 is the same as E1 over n-squared.
> 
> If we pull out the projection of the two line segments and the two areas, then we get two triangles that overlap each other. Like this. We'll call the length of the middle segment d, since it's the diameter of the circle A1. Since the triangles overlap like this, they're similar triangles, which means that the ratios of the side lengths are the same, so the length of the top segment is n times d, and this is the diameter of the perpendicular area.
> 
> Recall that the area of a circle is pi r-squared, which is the same as pi times half the diameter squared. So if the diameter increases by a factor of n, then the area increases by a factor of n squared. This means that our dA perpendicular is the same as dA one times n-squared.
> 
> Now we can cancel out the n-squared-s in the integral, and we have the exact same flux integral as the sphere. Which means that the electric flux through A2 must be equal to the electric flux through A1. And this will hold true for each dA as we integrate across the surface.
>
> Let's take a minute to imagine what would happen if we had some other charge inside the surface. We could surround it with a sphere and make the exact same flux arguments, and since the fluxes add, we would find that the flux would just now be the sum of the flux from each charge. So, we say that the flux must equal the total charge enclosed by the surface, divided by epsilon-naught.
> 
> If we have a charge that isn't enclosed by the surface, say, some charge over here, then it will have flux that goes both into and out of the surface, and using the same arguments as before, we would find that they are equal to each other, and so they end up cancelling out, leaving us with a net zero flux for charges outside the surface.
> 
> And now that we have Gauss's law, we can calculate electric field much more easily. Let's look at an example.

BLENDER 3D

> MC
> Let's say we have some infinite sheet of charge. The electric field on this sheet is going to point away from both the top and the bottom like this. So if we want to find the electric field some distance away from the sheet, we'll need to create a surface, like a cylinder. Now to simplify things, we'll just have one arrow for the electric field. And now we're ready to start.

Scene darkens, keeping BLENDER FREEZEFRAME in background with Manim overlay.
MANIM 2D

> MC
> As a reminder, here's Gauss's Law. We'll start by calculating the left side
> 
> Since we're at a constant distance from the charge and the electric field is perpendicular to the surfaces of the cylinder, the integral simplifies to just E times A. Where our A in this case is just the area of the top and bottom circle since the electric field doesn't go through the sides of the cylinder.
> So we get E times 2 pi r-squared.
> 
> Now to solve for the right-hand side we'll have to make some assumptions, specifically, we'll say that the whole sheet has a charge Q, and and area A. The charge density, sigma, is the charge per unit area, so Q over A, and if we want to get the charge we just have to multiply by the area of the region we want. So the charge enclosed is sigma, times pi r-squared, and don't forget to divide by epsilon-naught.

> Now when we set these two equal to each other, we can cancel out the pi r-squared and divide by two and we find that the electric field is equal to sigma over 2 epsilon-naught. That's it. No crazy integrals involved.



# Chapter 2: Circuits
## Voltage

INT. HOUSE BASEMENT -- DAY

> MC
> And now we have to talk about Voltage, which is like potential energy but for charges.

MANIM 2D

Square, force vectors, and equations.

> MC
> If I have some object, like a square, and I apply some force to it, and that force also causes it so move some distance, then I can find the work done as the force, times the distance, times the cosine of the angle between them.
> 
> So if the force and the distance are in the same direction, the work is just force times distance. If the force is perpendicular to the displacement, then there's no work. And if the force is in the opposite direction to the displacement, then you get negative force-times-distance work.

INT. HOUSE BASEMENT WALL -- DAY

Holding spherical object.

> MC
> If you think about the potential energy of this ball, it has the potential to fall down right now because I'm holding it up. Now if I hold it up higher, the potential energy increases, because it can fall down further. So mathematically, you have the force of gravity pointing downward, and when I pull it up, I'm moving it against the flow of gravity, which means that it now has the potential to flow in the opposite direction -- potential energy. This means that when I do negative work, I create potential energy.

MANIM 2D

> MC
> This means that when you do negative work, you get potential energy. U is the symbol we use for potential energy. We'll also rewrite the right side of the equation like this, just because it's a bit more compact. So now if the force changes as we move across the path of the object, then we can get the total potential energy by adding up the force times each displacement, if we make the displacements infinitesimally small, we'll get the best approximation. So our potential energy is written like this, the negative accumulation of the force across each displacement in the curve.
> 
> If we want to solve for the electric potential energy, then we just put in our electric force equation. The differential displacement, ds, will be in the r-hat direction, some infinitesimal radius dr. In other words, we're going to move the objects radially toward one another.
> 
> We'll start with the two charges infinitely far away from each other, because then they won't exert forces on each other, so there won't be any potential energy, and we'll bring them in to some radius r-prime.
> 
> Now we can solve this equation, and what we get is that the potential energy of two charges is the constant k, times charge 1, times charge 1, divided by the radius between them.
> 
> Now we're ready to talk about voltage because voltage is just the potential energy per unit charge. Just like electric field was asking "Hey, what kind of force would I get if I put a plus-one charge here?" Voltage is asking "hey, what's the potential energy if I put a plus-one charge here?" The voltage is equal to k, times the charge, divided by the radius.
> 
> If you look back to the equation on the top, you'll see that we can solve for voltage by dividing both sides by charge. So on the left side you get potential per unit charge, which is voltage, and on the right side we have a force, divided by charge, which is the same thing as electric field. So another way to think about voltage is that it's the negative accumulation of electric field as we move across some path. That means that if we take some charge, and we move it against the electric field, then we've created voltage because that charge now has the ability to flow along the electric field.
> 
> If we want the absolute voltage, we'll have to do the same thing where we go out from infinity to some radius r-prime, but if we just want the change in voltage between two points a and b, then we can just add up the accumulation from a to b.
> 	
> There's another thing to notice here. Remember how earlier we said that if the two vectors are perpendicular there's going to be no work done? The same thing applies here, and it tells us that if we move perpendicular to the electric field, then our voltage doesn't change.
> 
> If we go back to one of our old electric fields, and we draw lines perpendicular to the electric field, then everywhere along each line is going to be at the same voltage, which is why we call them equipotential lines -- same-voltage. If we want to, we can label these. Maybe the left side is negative one volt and the right side is positive one volt. And this has a lot of resemblance to a contour plot, except instead of elevation, you have voltage.

MANIM 2D

Black-and-white or faded out

> MC
> But what if our elevation **was** our voltage?

BLENDER 3D

Smooth fade transition from manim to Blender

> MC
> Well then we would have something like this, a kind of 3d map of the voltage. You can see that positive charges push up, creating hills, while negative charges pull down, making valleys.
> 
> Since the electric field points perpendicular to the contours, because the contours are perpendicular to the electric field, they're perpendicular to each other. Then the positive charge is going to follow the path of steepest descent.
>
> So if we bring in a positive charge at the top of a hill here, then the charge is going to roll downward because it's decreasing its voltage and its potential energy. 
> 
> Now if we put a negative charge at the bottom of this valley, it's going to roll upwards, because a very high voltage for it is actually a very negative, or very low, potential energy.
> 
> Another thing you can notice is that the charges don't actually care how high or how low the hill is, when the charge is rolling down the hill, the only thing that matters is that lower on the hill is lower down than where they are right now.
> 
> So if you have a 9-volt battery, what it really means is that one side has nine more volts of electric potential than the other end, not that it's at nine volts. And also, if you connect two of them together, one end must be nine volts higher than the other, but that other side also has to be nine volts higher than the final end. So end-to-end, you have 18 volts. Now also, if you take a piece of pencil lead and connect it between them, you'll see that it starts catching on fire, and the reason is that pencil lead has a very low-

MANIM 2D / 2D WITH TEXT

> MC
> -Resistance. But before we talk about that, let's take a minute to review what we've talked about so far.

## 4 Quantities

MANIM 2D

> MC
> Force is a push or pull on an object. Between two charged objects its equal to some constant, times each of the charges, divided by the square of the distance between them.
> Electric field is the force that would occur at some location if you were to put a +1 Charge there. One of the charges drops out of the equation, so we get a constant times q over the distance squared.
> Voltage is the electric parallel to potential energy. Specifically, it's the potential energy if you put a +1 charge at some location.
> Potential energy is the ability of some object to do work. When you push something against a force field, you create potential energy.
> We can get between electric field and force by adding or removing a charge, by multiplying or dividing by the charge.
> We can go between electric field and voltage by adding up the negative total accumulation of the electric field, or the slope of the voltage.
> We can get between voltage and potential energy by adding or removing the charge.
> And we can get between force and potential energy by adding up the accumulation, or looking at the slope.
> Take a minute to make sure you're comfortable with this, and especially these two quantities (E and V), since we'll be using them for the rest of the video.

## Resistance and Current

BLENDER 3D

Text stays on-screen

> MC
> So if I have a battery here, and I connect the two ends, then we would expect the electrons to move from one end to the other because that would decrease its potential energy. Now we also know that the electrons don't just all jump to the other end at once because, well, batteries don't burn out the second that you connect them, which means that there must be something stopping the electrons from just instantly jumping from one end to another, and that thing is resistance.
> 
> So resistance really measures the proportionality between the voltage applied and the flow of the electrons. But what exactly is the flow of electrons? well, one way to measure them is the amount of charge that passes through some area in a certain amount of time. So the change in charge over the change in time.
> 
> Now we could also define it geometrically. So the charge inside here is equal to the charge per volume times the volume. Seems simple enough. So we'll rewrite the charge per volume as the charge carrier density, so maybe 10 atoms per cubic centimeter, times the charge in each carrier, so maybe the charge on an electron, times the volume. And lastly we'll rewrite the volume as the area times the length, where the length is the velocity times some change in time. Why did we go through all this rewriting? It's because now we can just divide both sides by the change in time. And we get that the flow is equal to the number of charge carriers, times the charge on each carrier, times the cross-sectional area of a wire, times the velocity of each charge carrier. And by the way this flow is called current.
> 
> Now what we can also do is solve for the velocity of charges in a wire. So, let's do that.
> 
> We can solve for velocity by dividing both sides by n, q, and A. And now we'll pick some sensible values for each of these.

Note {citations 1 and 2}:
I = 10 Amperes (A)
12 Gauge wire: Diameter=2.05mm, Area=3.31mm^2=3.31e-6 m^2

Copper density {citations 3 and 4}:
n = (8.96 g/cm^3) x (6.02x10^23 atoms/mol) / (63.6g/mol) = 8.48 x 10^22 atoms/cm^3 = 8.48 x 10^28 atoms/m^3

Assume 1 free electron per atom:
q = e = 1.60 x 10^-19 C

v = I/(nqA) = 10/(3.31e-6 * 8.48e28 * 1.60e-19) = 2.23e-4 m/s or 0.223 mm/s

> MC
> If you do all of the calculations you get... 0.2 millimeters per second.

HOUSE BASEMENT BY LIGHT SWITCH

> MC
> But how can that be? I mean if I hit the light switch (turn off and on), they change almost instantly.

EDIT -- use the rubber duck as a light switch, film at sunset

BLENDER 3D

> MC
> Well, that's because when an electron moves into the circuit, it almost immediately starts pushing all of the others out of the way, so really the circuit is like a big conga line and when one goes into the circuit, another pops out almost instantly. So although the electrons move very slowly, the circuit can start and stop almost instantly.
> 
> And with a good idea of current, we can get back to resistance, because resistance is just how much voltage is required to get a certain amount of current out. For example, if my resistance is 2 ohms, then I need 2 volts to create 1 amp of current.
> 
> This equation that we've discovered is usually written like this, and it's called Ohm's law: voltage is equal to current times resistance, if we can find any two of these values, we can solve for the other.

INT. BASEMENT WALL
> MC
> So if you try to go an build a circuit usually you're going to get some resistors with different ratings, like these are around X ohms, and you insert them at different points in the circuit to control the current.

MANIM 2D

> MC
> So if I'm trying to build a circuit, I can start with a voltage source, and then I'll connect it to a resistor R1, and also a resistor R2, and lastly back to the voltage source. If R1 and R2 are different, then what is the current through the circuit going to look like?
> 
> To do that we can take a look at the geometric definition of a resistor. Remember that in practice a resistor makes it hard for the electrons to flow through by creating thermal energy. So if it's longer, then the electrons are going to have more resistor to go through before they reach the other end. But if it's wider, then there will be more paths for the electrons to go through, so they will flow through more easily.
> 
> So we can say that the resistance is proportional to the length of the resistor, and inversely proportional to the area of the resistor. Or that it's equal to some constant, times the length, divided by the area.
> 
> So when we put two resistors in series, one after the other, we're effectively creating a larger resistor with a larger length. Since the resistance is proportional to the length, we can get the effective resistance by just adding R1 and R2. So if our voltage is 9 , R1 is 1 , and R2 is 2 , Then the effective resistance if 3 Ohms, and the current through the circuit is 3 Amps.
>  
> Another way we can combine the resistors is like this, in parallel. Now, we're effectively increasing the area of the total resistor. Since the resistance is inversely proportional to the area, we add up the inverse of R1 and the inverse of R2, which gives us one over R-effective. So we can invert both sides one more time to get the effective resistance.
> 
> With these two methods, we can quickly break down the resistance of some complicated circuit.
> 
> R4 and R5 are in series, one after the other, so we can add them together. Now R45 and R6 are in parallel, so we add their inverses. R2 and R3 are also in parallel, so we can add their inverses. And lastly, we can add these three resistances, since they're all in series.

> MC
> Another useful metric in circuits is the power, or change in energy over change in time.
> So if the energy changes by 5 in 5 seconds, then your power is just one
> So we can get power by multiplying current, or change in charge over change in time, by voltage, or change in energy per unit charge.
> If we combine it with Ohm's law, you'll see that there are two other ways to write this.
> Now we can see why the battery caught on fire earlier.
> If we keep the voltage constant, then the power is inversely proportional to the resistance. So something that doesn't resist current flow that much will get a big spike in energy and as a result start smoking up. But not all of that current flow is equally distributed.
>
> When you have a parallel circuit like this, some of the current will go through the top path, and some will go through the bottom path, and they won't be exactly the same.
> Since charge is conserved, we know the that total current going in and out must be the same.
> And since energy is conserved, the change in voltage as you lose potential energy in the resistors must be the same.
> Using these two equations will usually work for you, but sometimes that's not enough, like in this circuit. In this case, you'll need to use the Kirchhoff equations. 
>
> The first one says that at a junction, the total charge going in must equal the total charge going out, because charge is conserved.
> 
> The second one tells you that if you start and end in the same place, you have to be at the same potential energy. So if I have a circuit like this, then I can draw a clockwise loop. When I move from positive to negative in the battery, my voltage increases by V, when I follow the flow of conventional current from positive to negative, I get a voltage drop in the resistor, equal to I times R. All of this must equal zero.


## Capacitors

MANIM 2D

> MC
> So far, we've been assuming a perfect battery, which means that we get a stable supply of voltage no matter what happens. In reality, sometimes voltage fluctuates (dropping slider that makes a light bulb go out and in?). So it's useful to create some system that can temporarily power our circuit during those fluctuations: a capacitor.
> 
> A capacitor is just a circuit component that has two disconnected sheets. When you connect it across a voltage source. Charges flow to the sheets since they're attracted to the other side. When they reach the sheets, the same-sign charges on the opposite side are repelled, so they continue across the circuit. However, now there is more positive charge on the positive sheet and negative charge on the negative sheet. Over time, this means that the capacitor will eventually reach equilibrium, and the voltage across the two plates will directly oppose the voltage created by the battery.
> 
> The quantity we use to measure capacitors is the capacitance, C, which is equal to how much charge, Q, you get on the plates when you apply some voltage, V.
> 
> If we want to know exactly how much charge is going to be on the capacitor over time then we can break it down with a Kirchhoff loop.
> So remember that means that the change in voltage over a full loop is zero.
> So the voltage from the battery, V, minus the voltage drop from the capacitor, which we can get from the C equals Q over V equation, is Q over C, minus the voltage drop from the resistor, I times R.
> Also remember that current is just the change in charge over change in time.
> Now we have a differential equation, and if we go ahead and solve it we get this exponential decay or carrying capacity function, which looks like this. So in the beginning the charge accumulates very quickly, and then it levels off over time. We can also look at the current, which is the slope of the charge curve. So in the beginning, a lot of charge is flowing through, and over time it goes to zero.
> 
> In a setup where we want the circuit to account for voltage fluctuations, we would put them in parallel like this. So when the battery is turned on, it first goes through the capacitor, charging it up, and then eventually diverts to the rest of the circuit. If the voltage source goes out, then current will continue to flow from the plates in the capacitor. We can go through the same procedure with a Kirchhoff loop equation, and we get the expected result of an exponential decay function: the capacitor starts with lots of charge and quickly dissipates it through the resistor.
> 
> We could also use the other ideas we've discussed to find the current through the resistor. But in general we can usually get away with thinking that the capacitor is going to act like a wire when it's first connected, getting all of the current, and like an open switch after a long time of being connected, with no current going through it.

INT. BASEMENT DAY
> MC
> But what happens if you connect two capacitors together?

MANIM 2D

> MC
> Once again, we'll take a look at a geometric definition for the parallel-plate capacitor. In this case, the area of each plate is A, and the distance between the plates is d
> 
> Recall from the earlier example that the electric field of a single plate is the charge density, sigma, over 2 epsilon naught. So for two plates, we get sigma over epsilon naught. Charge density is the same thing as charge over area, so we can rewrite this as Q over epsilon naught A.
> To get the (magnitude of the) voltage, we add up the accumulation of the electric field along some length, which simplifies to E times the length, since the electric field is constant. So our change in voltage is Q d over eps_0 A.
> Now remember that capacitance is charge divided by voltage, so if we plug in our voltage expression, we get that the capacitance is equal to epsilon naught A over d. In other words, it's proportional to the area and inversely proportional to the plate-to-plate distance.

(This is the basic process for any time you want to find the capacitance of a thing. Assume a charge Q, get the electric field with Gauss's Law, find voltage with $V = -\int \vec{E} \cdot d\vec{s}$, and then the capacitance with C = Q/V. The charges should end up cancelling in the end.)

> So if we have two capacitors in parallel, then we effectively have one big capacitor. Since the capacitance is proportional to the area, the effective capacitance is the sum of each parallel capacitor.
> If they're in series, then we're effectively increasing the plate-to-plate distance. Since distance is proportional to 1 over C, we add up the inverses of the capacitances, and invert the whole result to get the effective capacitance.
>
> Now sometimes it's useful to get the energy of a capacitor, and to do that, we can just add up voltage times charge, again using the C=Q/V equation. plugging in the capacitance equation, and we get several ways to write the energy. Now if you want to, you can rewrite the equations like this and divide by A times d, which is the volume, to get the energy density of the electric field. 

INT. BASEMENT DAY

> MC
> In a real capacitor the plates aren't exactly parallel, they're coiled up into a sort of cylindrical shape, and in between the plates, you put an insulating material, which is one that doesn't conduct electricity, to make it a more effective.
> To see why, let's take a look at what happens to the insulator when you insert it. While it can't conduct charges, the atoms can re-orient themselves, which means that they'll take this configuration. On the inside of the material, the plusses and minuses cancel, but on the outsides, you get a small electric field pointing like this, which opposes the electric field from the capacitor. Since voltage is derived from the electric field, a weaker electric field means less voltage. So now we have the same amount of charge on each plate, for less voltage, which means our capacitor is more effective.
>
> So basically the dielectric weakens the electric field by some factor, K (kappa). (E = E_{vacuum}xK = E_0 x K). And one way you can think of this is that it changes the permittivity constant from epsilon-naught to kappa times epsilon-naught. (Show Gauss's law thingymajig)

## AC Circuits

WALL OUTLET
> MC
> So I have a circuit right here, it's got some capacitors and some resistors, and it turns out that the wall outlet is actually a voltage source, so if I go ahead and plug this in-
> (house explosion)

2D TEXT + MANIMA
> MC
> Ok so it turns out that that voltage in your wall uses alternating current, so instead of the voltage looking like this, it looks like this (constant graph vs sine wave graph). 
> So some general AC circuit is gonna look like a normal sine wave, scaled up by a factor A, speed up by the angular frequency, omega, and shifted by a constant delta. In our case, we're going to ignore the phase shift delta to make the math slightly easier.
> V = IR still applies here, so if you've just got a resistor, then the current is going to line up with the voltage.
> Wall outlet voltages vary around the world but they're genrally around 100 to 300 volts, but there' s a problem here.
> How do we go from this wiggly sine graph to a constant number like 100?
> We can't just take the average of the graph, because it would just be zero.
> 
> Instead we square the sine wave, then take the average, then take the square root of that average. This is called the root mean square, or rms, and it's usually the quantity people are referring to in AC circuits.
> 
> So both ohm's law and the power equation are generally going to work when you're talking about rms quantities.
> 
> Now what if we have a capacitor?
> Well in a low-frequency situation, the capacitor is going to get to charge up, so it's going to oppose the current flow.
> But in a high frequency situation, it's not going to have time to fully charge up, so it's going to let more current through.
> So the opposition to AC current is inversely proportional to the frequency
> Also, the better capacitor you have, the more it's going to charge up and oppose the voltage, so it's also inversely proportional to the capacitance.
> 
> You can also get this from the definition of capacitance and the sine wave. In both cases it works out that the proportionality between resistance and current is this quantity 1 over omega C. It's like resistance, but it depends on how quickly the circuit is changing. It's called the reactance. So if you have a smaller capacitor or a more slowly-changing circuit, then there won't be as much max current when you apply some maximum voltage.
> 
> And because of these relations the current on the capacitor is always going to lead the voltage source by ninety degrees. To see why, lets walk through what is happening. When we first turn on the voltage, the capacitor acts like a wire, so it very quickly starts accumulating current. Then, the voltage starts to level off, and the current starts to level off too. The maximum charge stored on the capacitor occurs right here when we have the maximum voltage, you can see this since the charge is the area under the current curve. Now, when we start decreasing the voltage, the capacitor has excess charge to get rid of, so it starts discharging by sending current in the opposite direction. And it will keep discharging more and more until the voltage reaches zero. At this point, the areas under the curves cancel, which means that there's no charge on the capacitor right now. When the voltage starts going negative, the capacitor once again quickly starts charging up, since it acts like a wire, only now it's in the opposite direction, and the whole process repeats itself.
> 
> (show sine graph with the rotating unit circle).
> 
> A different way to imagine this is to show the sine waves as spinning vectors like this, where the vertical axis represents the voltage across the circuit.
> 
> So the voltage might look like this. The angle below is omega-t, and the height the voltage: v-naught sin of omega t
> A capacitor will be ninety degrees ahead, so we can show it right here like this.
> Now if we have a capacitor and a resistor in the same circuit, we know the resistor will follow the voltage. We also know that resistors in series add, so we can get the total resistance, in this case called the impedance since it also relies on the frequency. The magnitude of this impedance is equal to the length of the vectors added together. Since they're always perpendicular, it's the same as the hypotenuse of this right triangle.
> 
> 

WALL OUTLET
> MC
> And now that you know about AC you can connect stuff into the wall and you'll probably be ok. Maybe.
>  (shift to black, also show inductor mini callout thingy off to the side (slide it in or something (I love nested parentheticals))).

**(!!!!! smash bros new foe has appeared capacitor but it says a new component has appeared or something actually you should use this for the inductor !!!!)**
# Chapter 3: Magnetism

## Biot-Savart Law

ANIMATION 2D

> MC
> Some types of metals can be magnetized, which means they have a north pole and a south pole. Opposites attract and similar poles repel. And just like the electric field, we have a magnetic field, which tells us what would happen if we put a north pole there.

**(add something here about types of magnetism?)**

Now here's the thing.

> Moving charges also create magnetic fields. That's how the earth's magnetic field works. You can figure out how strong the magnetic field is going to be with the Biot-Savart law. Let's break this down.

$$d\vec{B} = \frac{\mu_0}{4\pi}\frac{I d\vec{l} \times \hat{r}}{r^2}$$
> The fraction out front is just a constant, so we're going to go ahead and ignore it for now. This cross symbol represents the cross product between the dL and r vectors. It's magnitude is the magnitudes of each of the vectors, times the sine of the angle between them. The direction can be found with the **right hand rule**.

MC FIRST PERSON

> Take your right hand, point straight forward, point your thumb up, and point your middle finger to the left. Now you have a right-hand rule. If a cross b equals c, then your pointer finger is the direction of a, your middle finger is the direction of b, and your thumb is the output, the direction of c.

MANIM 2D (BLENDER?)

> Back to the biot-savart law, this means that you can point your pointer finger in the direction of the wire, specifically, the direction that the positive charges go in, and your middle finger in the direction from the wire to the observation point, and your thumb points in the direction of the magnetic field.

> *At this point I feel like it's worth mentioning that conventionally, current goes in the direction of the positive charges, so the opposite direction of the electrons. Any time you see dL with the current, this is what it's referring to.*

> Lastly, the magnetic field is proportional to the current, so more current more magnetic field, and inversely proportional to r squared, so the further you are away, the weaker the magnetic field.

> Because of this law, the magnetic field is always going to curl around the wire of current like this. So another right hand rule you can do is a thumbs-up like this. Point your thumb in the direction that the positive charges move in, and your other fingers curl in the same direction as the magnetic field.

> Or if you want to, you can point your thumb in the direction of the magnetic field, and your fingers tell you the direction of the current.

> ==this means that if you want to create a fairly consistent magnetic field, you can get a loop of wire, like this==

> Putting it all together, to get the magnetic field from some running current, you add up the current times a small bit of length crossed with the radius, divided by the radius squared. In other words, moving charges create curling magnetic fields.

## Lorenz Force

> MC
> Now here's the weird thing:
> - Magnetic fields also move charges
> (chicken and egg moment)
> - Specifically, the force on a charge from a magnetic field is equal to q v cross b. This means that if the particle isn't moving, or the particle is moving completely parallel to the magnetic field, then there's no force. But once the particle starts moving slightly perpendicular to the magnetic field, then the charge experiences a force that's both perpendicular to its velocity and the magnetic field, specifically with the cross product

> Now in this segment we're gonna be working a lot with 3-dimensional vectors, which we usually represent as arrows. At the front of the arrow is a pointed tip, and the back of an arrow has what's called feathering. So, when an arrow points out of the screen, we draw it as a circle and a dot, like this. When an arrow points into the screen, then we use a circle with an x, which represents the feathering.

> -  So here's a question:
> 	- if I have an electron going out of the page and a magnetic field pointing to the right, what direction is the force going to be in? Now's your chance to figure it out ok time's up since force equals v cross b, we can point our index finger in the direction of the velocity, out of the page, and our middle finger to the right, this means that v cross b points upward, but remember that electrons have negative charge, so the upward-pointing force gets inverted and the electron actually experiences a downward force.
> Now that we know what forces act on a charge in a magnetic field the next logical thing to do might be tracing out its path in the field. Let's assume we have a magnetic field pointing into the screen, and we send a positive charge upward, using the force equation and the right hand rule, we can see that the force is to the left. So the charge will get pushed to the left until its trajectory looks like this. Now its velocity is to the left, so if we do the right hand rule again we get a downward force, which pushes the charge downward until its going down on the left like this. Now the force is to the right, so it goes like this, and then the force is up, causing the charge to complete its circular path.
> 
> It's important to note that the magnetic field the charge itself creates won't push the charge since each magnetic field force on one side has a direct equal and opposite force from the other side
> 
> If you have some general velocity in a straight magnetic field like this, you can break it into the components parallel and perpendicular to the magnetic field. The parallel component won't create any force, so the charge will keep going in that direction. The perpendicular component will curl the charge in a circular shape. So, when you combine them, most charges will follow a helical path when going through a magnetic field. This is how the northern lights work (wow crazy yippee).
> 
> Now of course this is only for a single charge. If you have a wire of charges, then we'll have the charge inside the wire. We've seen before that we can rewrite it with this geometric definition. If we let the length vector point in the same direction as the velocity vector, we can swap them since the magnitude and direction are both preserved, and now the constants on the outside are current. If the magnetic field changes across the wire, we can add up the force across tiny lengths of the wire like this.
>
> Here's a problem:
> I have a device that can measure voltage just fine, but I don't have anything to measure the magnetic field.
> What we can do is position the magnetic field perpendicular to the current of the circuit like this. Now the positive charges are pushed upwards. As more positive charges accumulate at the top, they create an electric field, which opposes the magnetic field force until they're equal. Once they're equal, we know that the magnetic field force is equal and opposite to the force from the electric field. So q times e should equal q v cross b. Since v and b are perpendicular, this simplifies to q v b, and we can cancel the Q's on both sides. 
> Now the voltage is the accumulation of the electric field. We'll assume the field is constant, in which case we get the voltage is equal to the electric field times this distance, or that the electric field is the voltage divided by the distance. Substituting this in, we can solve for the magnetic field in terms of the voltage. We can calculate the velocity like we did earlier, somewhere around 0.2 millimeters per second.

> Another example is two parallel wires like this (<---  | <---)
> The bottom wire creates a curling magnetic field, which points into the screen above it near the top wire, so our I dl cross b points downwards: the top wire gets pulled downwards.
> Likewise, the top wire creates a magnetic field pointing out of the screen near the bottom wire, so I dL cross b points upwards, so the wire points upwards. Parallel currents attract each other.

> As a third example, lets take a charged up capacitor, and add long wires extending from them to the left like this. Now we'll create a magnetic field pointing out of the screen with a permanent magnet. Lastly, we'll connect the circuit with a piece of wire that can move. With a small resistance, a large current gets drawn, this large I dL cross b then acts as a large force to the left (among us railgun)
> 
> For one last example , let's put a loop of current inside a magnetic field, like this. We want to compute the torque on the loop, which is the same as the radius crossed with the force. If you push from further away or with more force, you get more torque. Specifically, we'll want to get the torque that makes the loop spin on this top axis. The top and bottom wires both create vertical forces. Since those are parallel to our vertical axis, they don't create any torque (on that axis). We can now limit our focus to just these two vertical wires. Let's take a look at a top-down view. We'll rewrite the cross product as r times the force times the sine of the angle between them. The radius is half the width. Since our length is vertical and our magnetic field is horizontal, they're perpendicular, and the force is just I L times B, and we add the sine of the angle between them. The other wire will have the same torque, so added together we get this expression (w i L B sin(theta)). The width multiplied by the length is the same thing as the area, so combining them gives us this. Lastly, if we were to coil up the wire multiple times, then each coil would increase the magnetic field by the same amount. So we multiply by N, which represents the number of turns of the loop of wire.
> 
> 
> We'll collect each of these terms into a new vector, mu, which has magnitude NIA and points in the direction of an area vector, we get that the torque is equal to mu B sin theta, or Mu cross B. This works for any magnetic field we might have. And in fact this is generally the process used for building a motor.
## Ampere's Law

MANIM OR SOMETHING

> MC
> Earlier when we talked about electric field, we then went on to electric flux and then Gauss's Law. We can do the same thing here, but the result isn't that useful. Magnets always have a north pole and a south pole, if you cut one in half, you just get another north and south pole. So any region of space is going to have magnetic field flowing away from a north pole and towards a south pole. In other words, there will be flow into and out of it, and the exact amount makes it so the flux always cancels. The magnetic flux of any closed surface then is zero.
> 
> A more useful thing for calculating electric field is the electric circulation. Instead of looking at how much field flows through a surface, and thus how much it flows parallel to the area vector, we look at how much if it flows along a given path. Basically, at each point in the path we assign a length vector, dS, that points in the direction we're going. So for example if I have a wire of current here, you could imagine it would have a lot of circulation along this circle here.
> 
> Knowing the circulation allows us to use something called Ampere's Law (Am-pair). To see why it's useful, let's look at an example.
($$\oint \vec{B} \cdot d\vec{s}=\mu_0 I$$)

> If we go in a circle of constant radius around the wire, then the magnetic field will be constant, so just like Gauss's law we can pull it out, and now the integral of ds is the same as the length of the wire. Since it's a circle, we can use the circumference, 2 pi R. divide both sides by 2 pi R, and we get the magnetic field around a wire.

> Notice that instead of an inverse square law like we're used to seeing, the magnetic field decreases only inversely with radius. Thinking back to the biot-savart law, this is ultimately because we have a radius vector in the numerator, so magnitude wise, it will cancel with the r-squared, giving us effectively a magnetic field inversely proportional to the radius.

> The magnetic field still drops off pretty quickly, as you can see by looking at a graph of field strength and radius.

## Faraday's Law

> MC
> Alright now it's time to talk about how basically all major electricity sources generate that energy (except for photovoltaics (and chemical batteries but I wouldn't call those "major")).

> Are you ready for the secret?
> Take a piece of wire and wrap it up into a big coil.
> Then take a magnet and move it around inside that coil.
> That's it.
> If you can find some way to move the magnet or the coil, you got electricity.

> The mechanism behind this is called Faraday's law
> $$V=-\frac{d\phi_B}{dt}$$
> The voltage imposed on a loop of wire is equal to the negative of the change in flux over change in time. So if you increase the magnetic field, you get a voltage in the negative direction
> 
> If we want to break this equation up into its raw form, we'll write out the magnetic flux completely, as well as the voltage. In this case, it's conventional to not include the negative sign, so that the directions work out.

$$\int \vec{E} \cdot d\vec{l} = - \frac{d}{dt} \int \vec{B} \cdot d\vec{A}$$
> In this case, we're getting the magnetic flux through a loop, not a closed surface, which means that it won't be zero. Also, if you remember from earlier, we got this voltage equation from the force from the electric field, q times E. But we have a new force, too, q v cross B; so we have to add that to the equation:

$$\int (\vec{E} + \vec{v} \times \vec{B}) \cdot d\vec{l} = - \frac{d}{dt} \int \vec{B} \cdot d\vec{A}$$
> This equation isn't very easy to work with, so we'll stick with the original one.

> Any time I change the magnetic flux of my current loop, I get a voltage. Looking at the flux integral, there are three main ways we could do this. Make the magnetic field weaker or stronger, make the area bigger or smaller, or make the loop and magnetic field point more parallel or less parallel.

> Another thing to take note of is the negative sign. The direction that the voltage takes will oppose the changing flux. So if I have an increasing flux in this direction, then the voltage will point in the direction that would create an opposing magnetic field. This is called Lenz's law, or the "no you don't" law.

> You can use the right hand rule to figure out which direction the current is going to point in.

> First, determine which direction the magnetic flux is changing in. For example, if you start with a strong magnetic field upwards but it weakens, then your change vector is downwards. Now point it in the opposite direction, since the current opposes the change in flux. Point your thumb in that direction, and your fingers curl in the direction of current.

> One consequence of it is eddy currents.
> If you have a magnetic field, such as this one pointing into the screen. When you move a metal object into the magnetic field, the field through the metal gets stronger, pointing into the screen. To oppose this, voltage is created in the direction out of the screen -- counterclockwise. Now, there's also current in that direction. Most of which is pointing upwards as the object enters the magnetic field. Using our original right hand rule, we have upward current, and a magnetic field into the page, which creates a force pointing to the left on our piece of metal. This opposes the motion into the plate.
> 
> When the metal moves out of the plate, the magnetic field gets weaker, so the change vector points out of the screen. To oppose this, the voltage points into the screen, or clockwise, which also creates upward current and leftward force, opposing the motion out of the magnetic field.

INT. BASEMENT

> MC
> And now we're gonna talk about Tesla Coils

ANIMATION

> MC
> So the way Tesla coils work is by using something called a transformer.
> Let's say we have two coils stacked on top of each other like this. In the top coil, we turn on some current, which creates a magnetic field. In the second coil, as the magnetic field turns on, the magnetic flux changes, which means that we get voltage in the second coil. The magnetic field in both coils is the same, which means that the flux through each single loop should also be the same, and the change in flux over change in time should also be the same. Now the flux for an entire coil is equal to the flux for a single loop, times the number of loops. So the voltage on the first one is equal to the number of loops in the first one times the change in flux over change in time, and the voltage in the second one looks the same. We can solve for the change in flux over change in time in both cases, and we know that they're equal to each other. Solving this gives us that the voltage in the second coil is the same as the voltage in the first coil, times the ratio of the number of turns. So if we have more turns in our output coil, then we have more voltage.

> A tesla coil works by essentially combining two transformers together, giving us a very large voltage. Power is still conserved, though, so while our voltage is very high, our current isn't.


### Types of Magnetism

INT. BASEMENT?

> MC
> So far, we've been mostly talking about induced magnetism, which comes from moving charges. But as I'm sure you know, there are also certain objects that just act like magnets.

ANIMATION

> The things that we generally refer to as magnets are ferromagnetic. In general, they'll have different chunks that have magnetic fields pointing in certain directions, called domains. If you add in an external magnetic field, you can get these domains to align, giving you a permanent magnet. Examples of this material are Iron and Cobalt.

> The next type of magnetism is paramagnetism. The magnetic fields are usually randomly aligned, cancelling each other out, but if you add in an external magnetic field, the material will align with that, giving you a slight magnetic field. Examples of paramagnetic materials include Aluminum and Oxygen.

> Lastly, there's diamagnetism. To understand this, you can think of the electrons moving around the atom as tiny current loops which create tiny magnetic fields. In diamagnetic atoms, the electrons are paired up so that the magnetic field cancels out normally, but when you bring a magnet close to them, you get induction, so the current running in the direction opposing the magnetic field gets slightly stronger, and so the material slightly opposes the magnetic field.

> Examples of diamagnetic materials include water and most organic materials. If you can get a strong enough magnetic field, you can make things levitate, for example. We've been able to make a frog levitate with a strong magnet.

## Inductors and RL Circuits

ANIMATION

> MC
> Just like one of these coils of a transformer creates flux through the other coil, it also creates flux through itself.
> Specifically, that flux is proportional to the current that we send through the coil.

> and the voltage is proportional to the change in current over change in time.
> This is actually the secret 3rd circuit component that we didn't talk earlier: the inductor. Since it opposes changes in voltage, one way to think of it is to imagine one of those super big and heavy wheels on like a bank vault.

> When I start pushing clockwise, it takes a minute to get going, and once it's going, it will keep going, even if I start pushing it the other way

> Looking at the sine waves, it's going to lag behind the other voltages in the circuit, since it opposes changes in voltage. So we shift it to the right because, remember, further to the right means further into the future.

> If we start by looking at this peak right here, we can see that the voltage is at its maximum, at this point, enough voltage has been applied to get current running through the inductor, and it will keep running more and more as we push it more and more until we start pushing it in the other direction, then it will slow down more and more until again we're at the peak voltage on the other side, at which point the current starts flowing in the opposite direction, and it continues to do so until we push it the other way.

> The equivalent to resistance for an AC inductor is its reactance, which is equal to the frequency, times the inductance. In other words, a better inductor is better at opposing current, and the more quickly it switches, the more it will be opposed.

> If we look at the circular diagram, the vector for the inductor is 90 degrees behind the other things. If we have a resistor, a capacitor, and an inductor in series, then we can add them up and get the total impedance like this. It's the same thing as before, except now we have to subtract the reactance from the inductor, since it points opposite to the capacitor.

( energy)
> Since the capacitor is capable of resisting the voltage of an AC circuit, we would expect it to have some energy, and indeed it does. We can get it from a Kirchhoff loop. The voltage from the source minus the resistor voltage minus the inductor voltage. Since all of these quantities are voltage, if you multiply the whole thing by current, then each quantity becomes the power, because power is current times voltage. We can get the energy by adding up the power, or change in energy over change in time, over some interval of time. Doing this gives us 1/2 L i-squared

> One last thing about inductors.
> When you first turn on the voltage source, it's going to very much oppose the change in voltage, but over time, since the voltage stops changing, the inductor doesn't oppose it anymore. So in DC situations, you can think of an inductor as starting out like an open switch and then over time acting like a normal wire.


# Chapter 4: Electromagnetism

## Electromagnetic Waves


> So far we've seen four equations that pretty much tell us everything about electric and magnetic fields.
> Gauss's law relates the charge inside a closed surface to the flux through it.
> Gauss's Law for magnetism tells us we can't have a magnetic monopole.
> Ampere's Law tells us how running currents create curling magnetic fields.
> And faraday's law tells us how changing magnetic fields create voltage.

> Combining this with the force equation for charges gives us the basis of the theory of electromagnetism.

> But there's one small problem with how we've been writing Ampere's law so far.

> When we create a loop around our wire, we find the current through the loop as the charges flowing through any surface bounded by that loop.
> If I have a capacitor charging up with current, and I put a loop right here, then the current through this surface is the current on the wire, but the current through this surface is zero. Which means we have two different currents depending on which surface we choose.

> In order to fix this, we have to add something called the displacement current, which is epsilon-naught times the change in electric flux over change in time.
> This fixes our capacitor problem because while current is running, the capacitor is charging up, so there's changing electric flux through this surface, and current through this surface.

> This revision gives us this final set of equations, Maxwell's equations.

> There's another consequence of this addition to ampere's law.
> Let's say we have a vertical wire running some alternating current.
> 
> Because of ampere's law, this current creates a curling magnetic field.
> Because of faraday's law, this curling magnetic field creates an electric field right here.
> Because of our addition to ampere's law, this changing electric field creates a magnetic field, which creates an electric field, and it continues propegating in this direction.

> So as a recap, a charge by itself creates an electric field. A moving charge creates a magnetic field, and an accelerating charge creates an electromagnetic wave

> Now you can work backwards from Maxwell's equations if you want, and eventually you'll end up getting a form of the wave equation, just like we would expect. Essentially, if we assume that the points on this wave can only move up and down, then they should be accelerated in the direction of the curvature. So if it's curving down, then the wave gets accelerated downward. The proportionality between the curvature and the acceleration is the speed of the wave squared, so if you want to, you can plug in the constants we've been working with so far and you get that the speed of these waves in a vacuum is 3 x 10^8 meters per second, which is exactly equal to the speed of light in a vacuum.

> These connected electric and magnetic waves are actually the same thing as light waves.

> One useful solution to the wave equation looks like this
> It's just like the general sine wave in AC circuits we saw before, except now we have this k times x term. This is because the wave changes with both space and time. K is what's called the wave number, 2 x pi divided by the wavelength. When you multiply that by some length the wave has travelled, x, you get the angular length it travelled, which is the kind of input you want into a sine function.

> Some other useful things about this wave are the linear frequency, f, which tells you how many full cycles it goes through in a second. You can convert from angular to linear frequency with a factor of 2 times pi. The speed of the wave can also be written as the wavelength times the number of wavelengths that occur per second, or the wavelength times the frequency.

## Antennae

> We've already seen that electric and magnetic fields store energy, that's why standing in the sun heats you up. But another thing we can look at is the intensity of the wave, which is the power per area. So basically, the intensity is asking, how much energy per second we get on some square unit of area. And for a light wave it's equal to the magnitude of this vector, called the Poynting vector, which after some rewriting looks like this.

> Let's look at an example.
> Let's say I have a transmitter at a radio station with a power P, with some frequency f, that's a distance d away, and I have an antenna with length l. What's the maximum voltage I can get across my antenna?
> We can start by getting the intensity of the light wave, which is the power over area. If we assume it radiates in all directions, then the area is the area of the sphere, 4 pi d-squared. Now we can also get the intensity in terms of the electric field. So setting these two equal to each other allows us to solve for the maximum electric field. And now we can get the voltage from the electric field. We only care about the magnitude in this case, and since we want the maximum possible voltage, we'll assume that E and dl point in the same direction, so we just get E_0 times l, or this.

> Another type of antenna that you often see is a circular one like this; we'll call its radius r.
> So this one is gonna get voltage from the induction of the magnetic field, like the moving magnet that we saw earlier. We've seen before that these two constants (eps0 and mu0) are directly related to the speed of light, and they're built into Maxwell's equations in such a way that the induced electric and magnetic fields directly depend on them. Specifically for plane waves, it turns out that the ratio of electric and magnetic maximum field strength is equal to the speed of light. We've seen before that we can write up one of these fields like this, and now we can change the constants out front to include the maximum electric field, which is something we know. Since we're looking for maximum voltage, this integral will just simplify to the magnetic field times the area of the loop, pi r ^2. Now we have to get the time derivative of this, which introduces an omega into the equation, which is the same thing as 2 pi times the linear frequency. Low lastly, since we only want the maximum voltage, we'll consider just the amplitude of the sine wave, not the wave itself.

## Radiation Pressure

> Now one weird thing about light waves is that they actually carry momentum.
> This is the equation that we use for the momentum of an energy wave.
> The energy per volume of the wave is equal to the momentum per volume times the speed of light.
> This is actually a result from quantum physics, but there's still some kind of intuition you can get for where this comes from.
> So we know that momentum is mass times velocity, and also force is mass times acceleration, which means that force is the time derivative of momentum for constant mass, or we can rewrite that the momentum is the accumulation of the force over time.
> Now the energy is the accumulation of the force across some distance. Since we're dealing with changes in momentum, we'll assume that the force is in the same direction as the motion of the object. Now we can rewrite a small unit of length as the change in length over change in time times a small unit of length, and this differential right here is just the velocity. If the velocity is constant, which it is for a wave just floating around in free space, then we can pull it out, and now we have just the momentum integral. So the energy is equal in magnitude to the momentum times the velocity, which for a light wave is the speed of light.

> so we can plug in our energy density, which is twice the energy of one of the fields, and divide both sides by the speed of light. We'll rewrite the momentum per volume in this differential form. Now, if we have some chunk of volume, dV, it's the same as area times the length, which is the same as the speed times a small change in time. In other words, dV over dt is equal to the cross-sectional area times the speed of light. If we have the change in momentum per unit volume times the change in volume over change in time, then we can multiply them together to get the time derivative of momentum, or the force. Usually, we'll divide both sides by the area here, and instead write the pressure of an electromagnetic wave.

> Usually this isn't a whole lot of pressure, but it has the benefit of being kind of free energy. We've been able to make these solar sails that are propelled by sunlight.

## Geometric Optics

> Now we're gonna start tracing out the path of light waves.
> So when a light wave hits an interface between to materials, some of the light will usually be reflected. And it reflects in such a way that the angle to the surface normal is the same in both cases. So these two angles here are the same.
> 
> Most real objects don't look very reflective because they aren't this smooth. Instead they have a rough surface when you zoom in far enough, and so the light bounces in all sorts of directions.
> 
> Now one application of this is that if you get a reflective corner of material like this, then the reflected light is going to come out at the same angle that it came in at, which is pretty helpful if you want to send light waves back and forth. When we went to the moon we put some corner reflectors on it, and we can use those along with the speed of light to determine things like how quickly the moon is drifting away from us.
> 
> In addition to reflecting, some light is going to refract, or go through, the surface. Since light is no longer travelling in a vacuum, these two constants might change in the material, which will change the speed of light, so we define a quantity called the index of refraction, which is the ratio of the speed of light in a vacuum to the speed of light in this new material.
> 
> So when light enters a new medium, it bends according to Snell's law. The original index of refraction, times the sine of the incoming angle, is equal to the second index of refraction, times the sine of the outgoing angle.
> 
> In a real material, some of the light is going to reflect, and some is going to refract. And we can figure out the angles with the two laws we've seen before. But here's a problem: the larger I make my incoming angle, the larger the outgoing angle. If my incoming angle is large enough, then my outgoing angle can actually be larger than 90 degrees, which means that instead of refracting, all of the light gets reflected. We can calculate the angle this is going to happen at with Snell's law.
> 
> So let's take a look at an example:
> Water's index of refraction is about 4/3, and air's index refraction if roughly 1, so what angle do we need for an underwater light ray to start to have total internal reflection? We can start with Snell's law, we know the outgoing angle needs to be 90 degrees or larger, so for the smallest angle, we'll use 90 degrees. The sine of 90 is 1, so that term goes away, and now we can rearrange and we get that the angle is about 48.6 degrees.
> 
> But what if we went the other way?
> Well we could do the same steps, and we would get basically the same equation except now the fraction is flipped.
> 
> Remember that a sine wave looks like this
> We need to find the angle that gives us an output of 4/3, which is above the sine wave; in other words, it doesn't exist.
> There is no angle that will work for us to get total reflection from air to water. And in general, total internal reflection only works when you're going from a material of higher index to lower index of refraction.
> 
## Physical Optics

> Now in some cases you'll need to take into account the wave-like properties of light. One useful property is interference. When two waves meet at the same location, they add together. So if their peaks and valleys match up, or they're in phase, then the resultant wave is larger. This is called constructive interference. If they don't match up, then the resultant wave is smaller, this is called destructive interference.
> 
> One place this shows up is in double slit experiments. If we have a source area emitting light through these two slits. Since they're coming from the same source, we're assuming that they start out in phase. The difference between the lengths of the two paths will tell us if they're in phase or not. Specifically, if the path difference is an integer multiple of the wavelength, then they'll add constructively. If it's a half multiple of the wavelength, then they'll add destructively.
> 
> So what we see on a detector is certain bright spots where the waves add constructively because of the path length differences.
> 
> Another useful application of this is x-ray diffraction.
> If you have some kind of material that has a grid-like or lattice structure, and we shine some light waves onto the lattice, we'll assume that the light waves reflect off it like this. The difference in the path lengths is equal to the length of these two segments, or the distance between the atoms times the sine of angle one plus the distance times the sine of angle 2. So if we know the wavelength of the light and we send the light in at some specific angles, we can determine how far apart the atoms on the lattice are.

# Unit Rundown (Removed)

> ok so real quick all the stuff we've been talking about so far actually has units but I didn't wanna just like throw them all in there cause I thought it would be confusing but I also didn't want to not talk about them so here we go:
> 
> meters are out measure for how long something is
> 
> seconds are how we measure how long something takes to happen
> 
> so if you go some distance in some amount of time, like 3 meters per second, boom you got velocity
> 
> and now if you have some change in velocity over change in time, bam you have acceleration.
> 
> the kilogram is how we measure how much stuff something has
> 
> now we can use force equals mass times acceleration and plop in our units for mass and acceleration and boom, you have the newton, which is the unit for force
> 
> potential energy is the accumulation of force times distance, so the unit of energy is just a newton times a meter, or a Joule
> 
> Now for electrical charge there's the coulomb,
> 
> and for voltage there's the volt, which is just one joule of energy per coulomb of charge
> 
> electric field measures how much force you get if you were to put a one-coulomb charge there, so the units are newtons per coulomb
> 
> current is how much charge goes through in a certain amount of time, so coulombs per second, or amps
> 
> resistance is how much voltage is required to get a certain amount of current running, so we use volts per amp
> 
> capacitance is how much charge you get per volt, so one farad is one coulomb per volt
> 
> For magnetic field, you have the tesla, which is a newton per amp meter, which you can get from the q v b equation.
> 
> Inductance is how much magnetic flux you get per amp, so tesla meters squared per amp. The magnetic flux unit is also called Webers.

- Meter - unit of length
doorframe - 2 meters tall

- Second - base unit of time
heartbeat - ~ 1 second

- kg - base unit of mass
Pineapple : 2-3 kg

- velocity - m/s
walking speed: ~ 1.5 m/s

- acceleration - m/ s^2
gravity is 9.8 m/s^2

- N - unit of force
Isaac Newton
= kg m/s^2
apple weighs ~ 1N

- C - unit of charge
Charles-Augustin de Coulomb
lightning bolt is about 15 C
https://en.wikipedia.org/wiki/Lightning

- Volt - electric potential
Alessandro Volta
1 V = 1 J/C
AA battery is 1.5 volts

- Electric field is how much force per coulomb
So the units are just N/C

- Amp - current
André-Marie Ampère
1 A = 1 C / s
Households run ~10 A

- Ohm - resistance
Georg Ohm
1 ohm = 1 V/A
LED is ~200 ohms

- Farad - capacitance
Michael Faraday
1 Farad = 1 C / V

In Person
Most capacitors like these are on the order of microfarads
When I was in the physics lab they showed us a 1 farad capacitor and it was like the size of my forearm

- Tesla - Magnetic Field
Nikola Tesla

1 T = 1 N / (A x m)

F = q v B
{N} = {C m/s T}
{T} = {(N s)/(C m)} = {N/(A m)}
Force per amp of current and meter of running current
MRI machine is ~1-2 teslas

- Henry - Inductance
Joseph Henry
Magnetic flux per amp applied
phi_B = LI
T m^2 = H A
=>  1 H = 1 (T m^2)/A


(Magnetic flux is also referred to with Webers
Wilhelm Eduard Weber
1 H = 1 Wb/A)


