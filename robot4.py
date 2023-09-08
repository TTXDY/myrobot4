# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: D:\sunjieqiang\MyRobot\???5.SLDASM


import pychrono as chrono 
import builtins 

# some global settings: 
sphereswept_r = 0.001
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.003)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.003)
chrono.ChCollisionSystemBullet.SetContactBreakingThreshold(0.002)

shapes_dir = 'robot4_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('???4-1')
body_1.SetPos(chrono.ChVectorD(1.43378418365425,-1.81505050919978,-1.00190403400002))
body_1.SetRot(chrono.ChQuaternionD(0.658464850881657,-0.386763000796668,-0.218354900930672,-0.607585021711126))
body_1.SetMass(598.995410418289)
body_1.SetInertiaXX(chrono.ChVectorD(28.8252190084216,35.8932449234233,29.2403345860096))
body_1.SetInertiaXY(chrono.ChVectorD(-7.73313864193123,-4.63476944929171,-5.8497097993399))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.017129051176063,0.338890495356124,0.00766633603503142),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjFileShape() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFrameD(chrono.ChVectorD(-0.290026542952982,0.333825231013671,-0.276483873862302), chrono.ChQuaternionD(0.635149705566142,0.665504049894333,-0.265544265454151,0.28840155023491)))

# Visualization shape 
body_1_2_shape = chrono.ChObjFileShape() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_1.AddVisualShape(body_1_2_shape, chrono.ChFrameD(chrono.ChVectorD(-0.0706283930036322,0.08290601057078,-0.247824240297695), chrono.ChQuaternionD(0.635149705566142,0.665504049894333,-0.265544265454151,0.28840155023491)))

# Visualization shape 
body_1_3_shape = chrono.ChObjFileShape() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_1.AddVisualShape(body_1_3_shape, chrono.ChFrameD(chrono.ChVectorD(-0.225396623313272,0.335030332562498,-0.209188594715491), chrono.ChQuaternionD(0.781558699736659,0.48525950559722,-0.329300903063079,0.212720770813112)))

# Visualization shape 
body_1_1_shape = chrono.ChObjFileShape() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1.AddVisualShape(body_1_1_shape, chrono.ChFrameD(chrono.ChVectorD(0.254806243014257,0.343984284868008,0.290817998465462), chrono.ChQuaternionD(0.632044926334904,0.668453438917642,-0.26419888944669,0.289634524717996)))

# Visualization shape 
body_1_5_shape = chrono.ChObjFileShape() 
body_1_5_shape.SetFilename(shapes_dir +'body_1_5.obj') 
body_1.AddVisualShape(body_1_5_shape, chrono.ChFrameD(chrono.ChVectorD(-0.00453055356972754,0.0743012751620569,0.00083623937431776), chrono.ChQuaternionD(-0.0214637627129356,0.919701090461852,0.0161625410679865,0.391698842683648)))

# Visualization shape 
body_1_6_shape = chrono.ChObjFileShape() 
body_1_6_shape.SetFilename(shapes_dir +'body_1_6.obj') 
body_1.AddVisualShape(body_1_6_shape, chrono.ChFrameD(chrono.ChVectorD(-0.00198052809489646,-0.0567677294003175,-0.000633090699970085), chrono.ChQuaternionD(1,0,0,0)))

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('???4-3')
body_2.SetPos(chrono.ChVectorD(1.31409384877586,-1.80852472970175,-0.971966119998005))
body_2.SetRot(chrono.ChQuaternionD(0.703110229574695,0.311204730078014,-0.156144748423931,0.620005192384803))
body_2.SetMass(598.995410418289)
body_2.SetInertiaXX(chrono.ChVectorD(29.2403345860096,35.8932449234233,28.8252190084216))
body_2.SetInertiaXY(chrono.ChVectorD(5.8497097993399,-4.6347694492917,7.73313864193122))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-0.017129051176063,0.338890495356124,0.00766633603503142),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjFileShape() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_2.AddVisualShape(body_1_1_shape, chrono.ChFrameD(chrono.ChVectorD(-0.290026542952982,0.333825231013671,-0.276483873862302), chrono.ChQuaternionD(0.635149705566142,0.665504049894333,-0.265544265454151,0.28840155023491)))

# Visualization shape 
body_1_2_shape = chrono.ChObjFileShape() 
body_1_2_shape.SetFilename(shapes_dir +'body_1_2.obj') 
body_2.AddVisualShape(body_1_2_shape, chrono.ChFrameD(chrono.ChVectorD(-0.0706283930036324,0.0829060105707802,-0.247824240297695), chrono.ChQuaternionD(0.635149705566142,0.665504049894333,-0.265544265454151,0.28840155023491)))

# Visualization shape 
body_1_3_shape = chrono.ChObjFileShape() 
body_1_3_shape.SetFilename(shapes_dir +'body_1_3.obj') 
body_2.AddVisualShape(body_1_3_shape, chrono.ChFrameD(chrono.ChVectorD(-0.225396623313272,0.335030332562499,-0.209188594715491), chrono.ChQuaternionD(0.781558699736659,0.48525950559722,-0.329300903063079,0.212720770813112)))

# Visualization shape 
body_1_1_shape = chrono.ChObjFileShape() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_2.AddVisualShape(body_1_1_shape, chrono.ChFrameD(chrono.ChVectorD(0.254806243014257,0.343984284868008,0.290817998465462), chrono.ChQuaternionD(0.632044926334904,0.668453438917642,-0.264198889446691,0.289634524717996)))

# Visualization shape 
body_1_5_shape = chrono.ChObjFileShape() 
body_1_5_shape.SetFilename(shapes_dir +'body_1_5.obj') 
body_2.AddVisualShape(body_1_5_shape, chrono.ChFrameD(chrono.ChVectorD(-0.00453055356972776,0.0743012751620569,0.000836239374317982), chrono.ChQuaternionD(-0.0214637627129356,0.919701090461852,0.0161625410679865,0.391698842683648)))

# Visualization shape 
body_1_6_shape = chrono.ChObjFileShape() 
body_1_6_shape.SetFilename(shapes_dir +'body_1_6.obj') 
body_2.AddVisualShape(body_1_6_shape, chrono.ChFrameD(chrono.ChVectorD(-0.00198052809489702,-0.0567677294003173,-0.000633090699970085), chrono.ChQuaternionD(1,0,0,0)))

exported_items.append(body_2)




# Mate constraint: ????2 [MateProfileCenter] type:24 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: ???4-1/????-1/?-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: ???4-3/????-1/?-1 ,  SW ref.type:2 (2)

