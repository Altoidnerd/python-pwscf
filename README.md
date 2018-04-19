# python-pwscf

* classes for parsing and manipulating data from pw.x, and gipaw.x
  - ```md.Md(infile, outfile)``` is an object for fetching data from molecular dynamics simulations using pw.x
  - ```efg.Efg(outfile)``` is an object for fetching data from EFG calculations with gipaw.x
* ```namelist.Namelist()``` is for scripting the creation of input files for pw.x


![scrot](./img/8.png "")
#####A python wrapper for QE data creation/parsing that retains the expressiveness of the python language.
![scrot](./img/2.png "repr() looks like the the actual PW input file.")
![scrot]("./img/13.jpg" "Just print the object or return it as a string - it looks legitimate.")
![scrot](./img/3.png "Leverage the cleverness of python in a natural way to build pwscf input files. Syntax is pretty relaxed."  )
![scrot](./img/4.png )
![scrot](./img/1.png "This example is example01 under /PW/examples in the source QE distribution.")
![scrot](./img/5.png "repr() looks like the the actual PW input file.")
![scrot](./img/6.png " it doesn't care if you user uppercase or lowercase for you Namelist titles, but it does know what is and isn't a calif Namelist.")
![scrot](./img/7.png "Optional Title")

![scrot](./img/9.png "Optional Title")
![scrot](./img/10.png "Optional Title")



# python-pwscf
Python wrapper for QUANTUM ESPRESSO
