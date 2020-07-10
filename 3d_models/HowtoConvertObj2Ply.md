

### How to convert .obj to .ply, with colored vertices and triangular faces

1. open the meshlab and import *.obj file
2. centralize the mesh 
```
Filters -> Normals, Curvatures and Orientations ->
Transform: Move, Translate, Center -> 
check translate center of bbox to the origin -> Apply
```
3. subdivide mesh

```
Filters -> Remeshing, Simplication and Reconstruction -> 
Subdivision Surfaces:Midpoint -> Adjust Iterations and Apply
```

4. colorize vertexs using uv texture

```
Filters -> Color creation and Processing ->
Transfer Color:Texture to vertex
```

5. triangularize faces
```
Filters -> Polygonal and Quad Mesh -> Turn in to a Pure-Triangular Mesh
```

6. Export mesh as ply
```
File -> Export mesh as -> ply -> Check only color (vertice), Normal (vertice), Binary encoding.
'''


```



