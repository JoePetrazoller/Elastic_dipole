# Elastic_dipole

This script helps to calculate the elastic dipole of a substitutional point defect using lammps and a python post-treatment script.


To use it :
1. Find a potential for the system you want to evaluate (https://www.ctcms.nist.gov/potentials/).
2. Modify the "Step1.lammps" file, by changing the lattice parameter in the 4th line. Change the 11th line, "pair coeff" by writing the name of the chosen potential.
3. Modify the "Step2.lammps" file, by changing 11th line, "pair coeff".
4. Run the "Step1.lammps" file with lammps.
5. Copy the data of the last step of the calculation and paste it in a new file called "Step2_input". Change the atom type of any atom from "1" to "2".
7. Run the "Step2.lammps" file with lammps.
8. Copy the data of the last step of the calculation and paste it in a new file called "Step2_last_step".
9. Rename the log file "log_step2.lammps"
10. Open the Python file, change the point defect atom radius and run the script.
