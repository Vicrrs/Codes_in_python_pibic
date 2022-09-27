# Tutorial 2.2.2. Transport through a quantum wire
# ================================================
#
# Physics background
# ------------------
#  Conductance of a quantum wire; subbands
#
# Kwant features highlighted
# --------------------------
#  - Builder for setting up transport systems easily
#  - Making scattering region and leads
#  - Using the simple sparse solver for computing Landauer conductance

from matplotlib import pyplot
import kwant
import scipy.sparse.linalg as sla
# First, define the tight-binding system

syst = kwant.Builder()

# Here, we are only working with square lattices
a = 1
lat = kwant.lattice.square(a)

t = 1.0
M = 4
L = 20

# Define the scattering region

for i in range(L):
    for j in range(M):
        # On-site Hamiltonian
        syst[lat(i, j)] = 0

        # Hopping in y-direction
        if j > 0:
            syst[lat(i, j), lat(i, j - 1)] = -t

        # Hopping in x-direction
        if i > 0:
            syst[lat(i, j), lat(i - 1, j)] = -t

# Then, define and attach the leads:

# First the lead to the left
# (Note: TranslationalSymmetry takes a real-space vector)
sym_left_lead = kwant.TranslationalSymmetry((-a, 0))
left_lead = kwant.Builder(sym_left_lead)

for j in range(M):
    left_lead[lat(0, j)] = 0
    if j > 0:
        left_lead[lat(0, j), lat(0, j - 1)] = -t
    left_lead[lat(1, j), lat(0, j)] = -t



syst.attach_lead(left_lead)

# Then the lead to the right
sym_right_lead = kwant.TranslationalSymmetry((a, 0))
right_lead = kwant.Builder(sym_right_lead)

for j in range(M):
    right_lead[lat(0, j)] = 0
    if j > 0:
        right_lead[lat(0, j), lat(0, j - 1)] = -t
    right_lead[lat(1, j), lat(0, j)] = -t

syst.attach_lead(right_lead)

# Plot it, to make sure it's OK
kwant.plot(syst,num_lead_cells=6)


# Finalize the system
syst = syst.finalized()

#######################
#plot bands 
kwant.plotter.bands(left_lead.finalized(), show=False)
pyplot.xlabel("kx",fontsize=18)
pyplot.ylabel("Ef [t]",fontsize=18)
pyplot.show()
#######################333

# Now that we have the system, we can compute conductance
energies = []
data = []
energia_inicial = -4.0
energia_final = 4.0
numero_de_energias = 200
delta_energia = (energia_final-energia_inicial)/ numero_de_energias 
for ie in range(numero_de_energias):
    energy = energia_inicial + ie*delta_energia

    # compute the scattering matrix at a given energy
    smatrix = kwant.smatrix(syst, energy)

    # compute the transmission probability from lead 0 to
    # lead 1
    energies.append(energy)
    data.append(smatrix.transmission(1, 0))

# Use matplotlib to write output
# We should see conductance steps
pyplot.figure()
pyplot.plot(energies, data)
pyplot.xlabel("Ef [t]",fontsize = 18)
pyplot.ylabel("G [e^2/h]",fontsize=18)
pyplot.show()