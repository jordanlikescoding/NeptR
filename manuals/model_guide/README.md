many gazebo models will utilize meshes as a skin to put on their robot

we will assume you have knowledge of basic sdf model construction

make sure your model is in .stl format and is broken up into parts, when you export your model without sectioning it into pieces it will be exported as one mesh, you want multiple meshes

if required you can then import the model into blender to resize or simply any polygons present in the model

then make a folder that will hold your meshes somewhere in the project directory

to attach the mesh to a sdf structure the following syntax can be used

 <visual name="name">
    <geometry>
        <mesh>
            <uri>file:///path/to/your/model/some_name.stl</uri>
        </mesh>
    </geometry>

this syntax works for ignition gazebo, the syntax may differ for other versions of gazebo