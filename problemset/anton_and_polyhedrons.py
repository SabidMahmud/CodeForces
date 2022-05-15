# Tetrahedron = 4 #triangular faces.
# Cube = 6 #square faces.
# Octahedron = 8 #triangular faces.
# Dodecahedron = 12 #pentagonal faces.
# Icosahedron = 20 #triangular faces.

n = int( input() )

faces = 0
while n > 0 :
    n -= 1
    polyhedron = input()
    if polyhedron == "Tetrahedron" :
        faces += 4
    elif polyhedron == "Cube" :
        faces += 6
    elif polyhedron == "Octahedron" :
        faces += 8
    elif polyhedron == "Dodecahedron" :
        faces += 12
    elif polyhedron == "Icosahedron" :
        faces += 20
    else :
        continue

print ( faces )
