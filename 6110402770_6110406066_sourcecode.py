bl_info = {
    "name": "Add Image_Processing",
    "author": "By TNK",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tools > Image_Processing",
    "description": "Add Image_Processing with Plane",
    "warning": "",
    "doc_url": "",
    "category": "3D VIEW",
}


import bpy
from bpy import context, data, ops

def create_poster(group_name):
    bpy.context.scene.use_nodes = True
    test_group = bpy.data.node_groups.new('OilPosters', 'CompositorNodeTree')
    # create group inputs
    group_inputs = test_group.nodes.new('NodeGroupInput')
    group_inputs.location = (-350,0)
    test_group.inputs.new('NodeSocketImage','Image')
    test_group.inputs.new('NodeSocketFloat','Top')
    test_group.inputs.new('NodeSocketFloat','Middle')
    test_group.inputs.new('NodeSocketFloat','Bottom')
    # create group outputs
    group_outputs = test_group.nodes.new('NodeGroupOutput')
    group_outputs.location = (550,0)
    test_group.outputs.new('NodeSocketImage','Image')

    # create three math nodes in a group
    node_mul = test_group.nodes.new('CompositorNodeMath')
    node_mul.operation = 'MULTIPLY'
    node_mul.location = (-200,100)

    node_sub = test_group.nodes.new('CompositorNodeMath')
    node_sub.operation = 'SUBTRACT'
    node_sub.location = (-50,-100)

    node_round = test_group.nodes.new('CompositorNodeMath')
    node_round.operation = 'ROUND'
    node_round.location = (100,100)

    node_divide = test_group.nodes.new('CompositorNodeMath')
    node_divide.operation = 'DIVIDE'
    node_divide.location = (250,-100)

    node_mix = test_group.nodes.new('CompositorNodeMixRGB')
    node_mix.blend_type = 'DIVIDE'
    node_mix.inputs[0].default_value = 0.5
    node_mix.location = (400,100)

    # link nodes together
    test_group.links.new(node_mul.outputs[0], node_sub.inputs[0])
    test_group.links.new(node_sub.outputs[0], node_round.inputs[0])
    test_group.links.new(node_round.outputs[0], node_divide.inputs[0])
    test_group.links.new(node_divide.outputs[0], node_mix.inputs[2])


    # link inputs
    test_group.links.new(group_inputs.outputs[0], node_mix.inputs[1])
    test_group.links.new(group_inputs.outputs[0], node_mul.inputs[0])
    test_group.links.new(group_inputs.outputs['Top'], node_mul.inputs[1])
    test_group.links.new(group_inputs.outputs['Middle'], node_sub.inputs[1])
    test_group.links.new(group_inputs.outputs['Bottom'], node_divide.inputs[1])

    test_group.inputs['Top'].default_value = 7.2
    test_group.inputs['Middle'].default_value = 0.5
    test_group.inputs['Bottom'].default_value = 5

    #glossinessFactorInput.min_value 
    #link output
    test_group.links.new(node_mix.outputs[0], group_outputs.inputs['Image'])
    return test_group

def create_sketch(group_name):
    # create a group
    #for a in bpy.data.node_groups:
    #    bpy.data.node_groups.remove(a, do_unlink=True)

    bpy.context.scene.use_nodes = True
    test_group = bpy.data.node_groups.new('Sketch', 'CompositorNodeTree')
    # create group inputs
    group_inputs = test_group.nodes.new('NodeGroupInput')
    group_inputs.location = (-350,0)
    test_group.inputs.new('NodeSocketImage','Image')
    test_group.inputs.new('NodeSocketFloat','Thickness')
    test_group.inputs.new('NodeSocketFloat','Color')

    # create group outputs
    group_outputs = test_group.nodes.new('NodeGroupOutput')
    group_outputs.location = (550,0)
    test_group.outputs.new('NodeSocketImage','Image')

    # create three math nodes in a group
    node_fil = test_group.nodes.new('CompositorNodeFilter')
    node_fil.filter_type = 'SHARPEN'
    node_fil.location = (-200,100)

    node_add = test_group.nodes.new('CompositorNodeMath')
    node_add.operation = 'GREATER_THAN'
    node_add.inputs[1].default_value = 0.5
    node_add.location = (-50,-100)
    
    node_mix = test_group.nodes.new('CompositorNodeMixRGB')
    node_mix.blend_type = 'SCREEN'
    node_mix.location = (400,100)
    
    node_ramp = test_group.nodes.new('CompositorNodeValToRGB')
    node_ramp.location = (400,100)
    node_ramp.color_ramp.elements[0].color = (0,0,0,1)
    node_ramp.color_ramp.elements[1].color = (1,1,1,1)
    node_ramp.color_ramp.elements[0].position = (0.029)
    node_ramp.color_ramp.elements[1].position = (0.069)
    # link nodes together
    test_group.links.new(node_fil.outputs[0], node_ramp.inputs[0])
    test_group.links.new(node_ramp.outputs[0], node_add.inputs[0])
    test_group.links.new(node_add.outputs[0], node_mix.inputs[1])

    # link inputs
    test_group.links.new(group_inputs.outputs[0], node_fil.inputs[1])
    test_group.links.new(group_inputs.outputs[1], node_fil.inputs[0])
    test_group.links.new(group_inputs.outputs[0], node_mix.inputs[2])
    test_group.links.new(group_inputs.outputs[2], node_mix.inputs[0])

    test_group.inputs[1].default_value = 1.133
    test_group.inputs[2].default_value = 0.5

    #glossinessFactorInput.min_value 
    #link output
    test_group.links.new(node_mix.outputs[0], group_outputs.inputs['Image'])
    return test_group
# create a group
#for a in bpy.data.node_groups:
#    bpy.data.node_groups.remove(a, do_unlink=True)
def create_temp(group_name):
    bpy.context.scene.use_nodes = True
    test_group = bpy.data.node_groups.new('Temperature', 'CompositorNodeTree')
    # create group inputs
    group_inputs = test_group.nodes.new('NodeGroupInput')
    group_inputs.location = (-350,0)
    test_group.inputs.new('NodeSocketImage','Image')
    test_group.inputs.new('NodeSocketFloat','Coolness')
    test_group.inputs.new('NodeSocketFloat','Warmth')
    test_group.inputs.new('NodeSocketFloat','Strength')

    # create group outputs
    group_outputs = test_group.nodes.new('NodeGroupOutput')
    group_outputs.location = (550,0)
    test_group.outputs.new('NodeSocketImage','Image')

    # create three math nodes in a group
    node_bal1 = test_group.nodes.new('CompositorNodeColorBalance')
    node_bal1.correction_method = 'LIFT_GAMMA_GAIN'
    node_bal1.lift = (0.837, 0.880, 1.0)
    node_bal1.gamma = (0.945, 0.968, 1.0)
    node_bal1.gain =  (1.1, 1.1, 1.1)
    node_bal1.location = (-200,200)

    node_bal2 = test_group.nodes.new('CompositorNodeColorBalance')
    node_bal2.correction_method = 'LIFT_GAMMA_GAIN'
    node_bal2.lift = (1.0, 0.880, 0.8)
    node_bal2.gamma = (1.2, 1.0, 0.64)
    node_bal2.gain =  (1.34, 1.11, 1.0)
    node_bal2.location = (0,-200)
    
    node_mix1 = test_group.nodes.new('CompositorNodeMixRGB')
    node_mix1.blend_type = 'MIX'
    node_mix1.location = (200,100)

    node_mix2 = test_group.nodes.new('CompositorNodeMixRGB')
    node_mix2.blend_type = 'MIX'
    node_mix2.location = (400,100)

    # link nodes together
    test_group.links.new(node_bal1.outputs[0], node_mix1.inputs[1])
    test_group.links.new(node_bal2.outputs[0], node_mix1.inputs[2])
    test_group.links.new(node_mix1.outputs[0], node_mix2.inputs[2])

    ## link inputs
    test_group.links.new(group_inputs.outputs[0], node_bal1.inputs[1])
    test_group.links.new(group_inputs.outputs[0], node_bal2.inputs[1])
    test_group.links.new(group_inputs.outputs[0], node_mix2.inputs[1])
    test_group.links.new(group_inputs.outputs[1], node_bal1.inputs[0])
    test_group.links.new(group_inputs.outputs[2], node_mix1.inputs[0])
    test_group.links.new(group_inputs.outputs[2], node_bal2.inputs[0])
    test_group.links.new(group_inputs.outputs[3], node_mix2.inputs[0])

    test_group.inputs[1].default_value = 1.133
    test_group.inputs[2].default_value = 0.453
    test_group.inputs[3].default_value = 1.0

    #glossinessFactorInput.min_value 
    #link output
    test_group.links.new(node_mix2.outputs[0], group_outputs.inputs['Image'])
    return test_group

def create_highpass(group_name):
    bpy.context.scene.use_nodes = True
    test_group = bpy.data.node_groups.new('HighPass', 'CompositorNodeTree')
    # create group inputs
    group_inputs = test_group.nodes.new('NodeGroupInput')
    group_inputs.location = (-350,0)
    test_group.inputs.new('NodeSocketImage','Image')
    test_group.inputs.new('NodeSocketFloat','Radius')

    # create group outputs
    group_outputs = test_group.nodes.new('NodeGroupOutput')
    group_outputs.location = (550,0)
    test_group.outputs.new('NodeSocketImage','Image')

    # create three math nodes in a group
    node_blur = test_group.nodes.new('CompositorNodeBlur')
    node_blur.filter_type = 'FLAT'
    node_blur.use_relative = True
    node_blur.factor_x = 10
    node_blur.factor_y = 10
    node_blur.location = (-200,200)

    node_invert = test_group.nodes.new('CompositorNodeInvert')
    node_invert.invert_rgb = True
    node_invert.inputs[0].default_value = 1

    node_mix = test_group.nodes.new('CompositorNodeMixRGB')
    node_mix.blend_type = 'MIX'
    node_mix.inputs[0].default_value = 0.5

    # link nodes together
    test_group.links.new(node_invert.outputs[0], node_blur.inputs[0])
    test_group.links.new(node_blur.outputs[0], node_mix.inputs[1])

    ## link inputs
    test_group.links.new(group_inputs.outputs[0], node_invert.inputs[1])
    test_group.links.new(group_inputs.outputs[0], node_mix.inputs[2])
    test_group.links.new(group_inputs.outputs[1], node_blur.inputs[1])


    test_group.inputs[1].default_value = 1

    #glossinessFactorInput.min_value 
    #link output
    test_group.links.new(node_mix.outputs[0], group_outputs.inputs['Image'])
    return test_group

def create_img_process(group_name):
    bpy.context.scene.use_nodes = True
    test_group = bpy.data.node_groups.new('ImgProcess', 'CompositorNodeTree')
    # create group inputs
    group_inputs = test_group.nodes.new('NodeGroupInput')
    group_inputs.location = (-350,0)
    test_group.inputs.new('NodeSocketImage','Image')
    test_group.inputs.new('NodeSocketFloat','Thickness')
    test_group.inputs.new('NodeSocketFloat','Coolness')
    test_group.inputs.new('NodeSocketFloat','Warmth')

    # create group outputs
    group_outputs = test_group.nodes.new('NodeGroupOutput')
    group_outputs.location = (550,0)
    test_group.outputs.new('NodeSocketImage','Image')

    # create three math nodes in a group
    node_blur = test_group.nodes.new('CompositorNodeBlur')
    node_blur.filter_type = 'FLAT'
    node_blur.size_x = 10
    node_blur.size_y = 10
    node_blur.location = (-200,200)

    node_mul1 = test_group.nodes.new('CompositorNodeMixRGB')
    node_mul1.blend_type = 'MULTIPLY'
    node_mul1.inputs[0].default_value = 0.78
    node_mul1.location = (-200, 0)

    node_mul2 = test_group.nodes.new('CompositorNodeMixRGB')
    node_mul2.blend_type = 'MULTIPLY'
    node_mul2.location = (0, 0)

    node_skt = test_group.nodes.new('CompositorNodeGroup')
    node_skt.node_tree = create_sketch('skt')
    node_skt.location = (100, 0)

    node_tmp = test_group.nodes.new('CompositorNodeGroup')
    node_tmp.node_tree = create_temp('tmp')
    node_tmp.location = (200, 0)

    node_de1 = test_group.nodes.new('CompositorNodeDenoise')
    node_de1.use_hdr = True
    node_de1.location = (-100, 300)

    node_de2 = test_group.nodes.new('CompositorNodeDenoise')
    node_de2.use_hdr = True
    node_de2.location = (300, 300)

    # link nodes together
    test_group.links.new(node_de1.outputs[0], node_skt.inputs[0])
    test_group.links.new(node_blur.outputs[0], node_mul1.inputs[2])
    test_group.links.new(node_mul1.outputs[0], node_mul2.inputs[2])
    test_group.links.new(node_mul2.outputs[0], node_tmp.inputs[0])
    test_group.links.new(node_skt.outputs[0], node_mul2.inputs[1])
    test_group.links.new(node_tmp.outputs[0], node_de2.inputs[0])

    # link inputs
    test_group.links.new(group_inputs.outputs[0], node_de1.inputs[0])
    test_group.links.new(group_inputs.outputs[0], node_mul1.inputs[1])
    test_group.links.new(group_inputs.outputs[0], node_blur.inputs[0])
    test_group.links.new(group_inputs.outputs[1], node_skt.inputs[1])
    test_group.links.new(group_inputs.outputs[2], node_tmp.inputs[1])
    test_group.links.new(group_inputs.outputs[3], node_tmp.inputs[2])


    test_group.inputs[1].default_value = 1.133
    test_group.inputs[2].default_value = 0.453
    test_group.inputs[3].default_value = 0.307

    #glossinessFactorInput.min_value 
    #link output
    test_group.links.new(node_de2.outputs[0], group_outputs.inputs['Image'])
    return test_group

def create_V1(group_name):
    bpy.context.scene.use_nodes = True
    test_group = bpy.data.node_groups.new('V1', 'CompositorNodeTree')
    # create group inputs
    group_inputs = test_group.nodes.new('NodeGroupInput')
    group_inputs.location = (-350,0)
    test_group.inputs.new('NodeSocketImage','Image')
    test_group.inputs.new('NodeSocketFloat','Saturation')
    test_group.inputs.new('NodeSocketFloat','Value')
    test_group.inputs.new('NodeSocketFloat','Thickness')
    test_group.inputs.new('NodeSocketFloat','Coolness')
    test_group.inputs.new('NodeSocketFloat','Warmth')

    # create group outputs
    group_outputs = test_group.nodes.new('NodeGroupOutput')
    group_outputs.location = (550,0)
    test_group.outputs.new('NodeSocketImage','Image')

    # create three math nodes in a group
    node_hue = test_group.nodes.new('CompositorNodeHueSat')
    node_hue.inputs[1].default_value = 0.5
    node_hue.inputs[4].default_value = 1
    node_hue.location = (-300,200)

    node_poster = test_group.nodes.new('CompositorNodeGroup')
    node_poster.node_tree = create_poster('poster')
    node_poster.inputs[1].default_value = 3.6
    node_poster.inputs[2].default_value = -2.9
    node_poster.inputs[3].default_value = 5.7
    node_poster.location = (0,200)

    node_img_process = test_group.nodes.new('CompositorNodeGroup')
    node_img_process.node_tree = create_img_process('img_process')
    node_img_process.location = (300,200)

    # link nodes together
    test_group.links.new(node_hue.outputs[0], node_poster.inputs[0])
    test_group.links.new(node_poster.outputs[0], node_img_process.inputs[0])

    ## link inputs
    test_group.links.new(group_inputs.outputs[0], node_hue.inputs[0])
    test_group.links.new(group_inputs.outputs[1], node_hue.inputs[2])
    test_group.links.new(group_inputs.outputs[2], node_hue.inputs[3])
    test_group.links.new(group_inputs.outputs[3], node_img_process.inputs[1])
    test_group.links.new(group_inputs.outputs[4], node_img_process.inputs[2])
    test_group.links.new(group_inputs.outputs[5], node_img_process.inputs[3])

    test_group.inputs[1].default_value = 1.040
    test_group.inputs[2].default_value = 0.733
    test_group.inputs[3].default_value = 1.133
    test_group.inputs[4].default_value = 0.453
    test_group.inputs[5].default_value = 0.307

    #glossinessFactorInput.min_value 
    #link output
    test_group.links.new(node_img_process.outputs[0], group_outputs.inputs['Image'])
    return test_group

def create_V2(group_name):
    bpy.context.scene.use_nodes = True
    test_group = bpy.data.node_groups.new('V2', 'CompositorNodeTree')
    # create group inputs
    group_inputs = test_group.nodes.new('NodeGroupInput')
    group_inputs.location = (-350,0)
    test_group.inputs.new('NodeSocketImage','Image')
    test_group.inputs.new('NodeSocketImage','ImageRamp')
    test_group.inputs.new('NodeSocketFloat','Thickness')
    test_group.inputs.new('NodeSocketFloat','Saturation')
    test_group.inputs.new('NodeSocketFloat','Value')
    test_group.inputs.new('NodeSocketFloat','Coolness')
    test_group.inputs.new('NodeSocketFloat','Warmth')

    # create group outputs
    group_outputs = test_group.nodes.new('NodeGroupOutput')
    group_outputs.location = (550,0)
    test_group.outputs.new('NodeSocketImage','Image')

    # create three math nodes in a group
    node_highpass = test_group.nodes.new('CompositorNodeGroup')
    node_highpass.node_tree = create_highpass('highpass')
    node_highpass.inputs[1].default_value = 1
    node_highpass.location = (-300,200)

    node_skt = test_group.nodes.new('CompositorNodeGroup')
    node_skt.node_tree = create_sketch('sketch')
    node_skt.inputs[2].default_value = 0
    node_skt.location = (-200,200)

    node_de = test_group.nodes.new('CompositorNodeDenoise')
    node_de.use_hdr = True
    node_de.location = (-100, 300)

    node_mul1 = test_group.nodes.new('CompositorNodeMixRGB')
    node_mul1.blend_type = 'MULTIPLY'
    node_mul1.inputs[0].default_value = 1
    node_mul1.location = (0, 0)

    node_mul2 = test_group.nodes.new('CompositorNodeMixRGB')
    node_mul2.blend_type = 'MULTIPLY'
    node_mul2.inputs[0].default_value = 1
    node_mul2.location = (100, 0)

    node_hue = test_group.nodes.new('CompositorNodeHueSat')
    node_hue.inputs[1].default_value = 0.5
    node_hue.inputs[4].default_value = 1
    node_hue.location = (100,300)

    node_temp = test_group.nodes.new('CompositorNodeGroup')
    node_temp.node_tree = create_temp('temp')
    node_temp.inputs[3].default_value = 1.2
    node_temp.location = (200,200)
    
    # link nodes together
    test_group.links.new(node_highpass.outputs[0], node_skt.inputs[0])
    test_group.links.new(node_skt.outputs[0], node_de.inputs[0])
    test_group.links.new(node_de.outputs[0], node_mul1.inputs[1])
    test_group.links.new(node_mul1.outputs[0], node_mul2.inputs[1])
    test_group.links.new(node_mul2.outputs[0], node_temp.inputs[0])
    test_group.links.new(node_hue.outputs[0], node_mul2.inputs[2])


    ## link inputs
    test_group.links.new(group_inputs.outputs[0], node_highpass.inputs[0])
    test_group.links.new(group_inputs.outputs[0], node_hue.inputs[0])
    test_group.links.new(group_inputs.outputs[1], node_mul1.inputs[2])
    test_group.links.new(group_inputs.outputs[2], node_skt.inputs[1])
    test_group.links.new(group_inputs.outputs[3], node_hue.inputs[2])
    test_group.links.new(group_inputs.outputs[4], node_hue.inputs[3])
    test_group.links.new(group_inputs.outputs[5], node_temp.inputs[1])
    test_group.links.new(group_inputs.outputs[6], node_temp.inputs[2])

    test_group.inputs[2].default_value = 5.933
    test_group.inputs[3].default_value = 1.547
    test_group.inputs[4].default_value = 1.507
    test_group.inputs[5].default_value = 1.133
    test_group.inputs[6].default_value = -0.447

    #glossinessFactorInput.min_value 
    #link output
    test_group.links.new(node_temp.outputs[0], group_outputs.inputs['Image'])
    return test_group

def create_V3(group_name):
    bpy.context.scene.use_nodes = True
    test_group = bpy.data.node_groups.new('V3', 'CompositorNodeTree')
    # create group inputs
    group_inputs = test_group.nodes.new('NodeGroupInput')
    group_inputs.location = (-350,0)
    test_group.inputs.new('NodeSocketImage','Image')
    test_group.inputs.new('NodeSocketImage','ImageRamp')
    test_group.inputs.new('NodeSocketImage','ImageOver')
    test_group.inputs.new('NodeSocketFloat','Coolness')
    test_group.inputs.new('NodeSocketFloat','Warmth')

    # create group outputs
    group_outputs = test_group.nodes.new('NodeGroupOutput')
    group_outputs.location = (550,0)
    test_group.outputs.new('NodeSocketImage','Image')

    # create three math nodes in a group
    
    node_rgb2bw = test_group.nodes.new('CompositorNodeRGBToBW')
    node_rgb2bw.location = (-300, 300)
    
    node_poster = test_group.nodes.new('CompositorNodeGroup')
    node_poster.node_tree = create_poster('poster')
    node_poster.inputs[1].default_value = 4.2
    node_poster.inputs[2].default_value = 0.7
    node_poster.inputs[3].default_value = 5.0
    node_poster.location = (-200,200)

    node_de = test_group.nodes.new('CompositorNodeDenoise')
    node_de.use_hdr = True
    node_de.location = (-100, 300)

    node_mul1 = test_group.nodes.new('CompositorNodeMixRGB')
    node_mul1.blend_type = 'MULTIPLY'
    node_mul1.inputs[0].default_value = 1
    node_mul1.location = (0, 0)

    node_mul2 = test_group.nodes.new('CompositorNodeMixRGB')
    node_mul2.blend_type = 'MULTIPLY'
    node_mul2.inputs[0].default_value = 1
    node_mul2.location = (100, 0)

    node_temp = test_group.nodes.new('CompositorNodeGroup')
    node_temp.node_tree = create_temp('temp')
    node_temp.inputs[3].default_value = 0.3
    node_temp.location = (200,200)
    
    # link nodes together
    test_group.links.new(node_rgb2bw.outputs[0], node_poster.inputs[0])
    test_group.links.new(node_poster.outputs[0], node_de.inputs[0])
    test_group.links.new(node_de.outputs[0], node_mul1.inputs[1])
    test_group.links.new(node_mul1.outputs[0], node_mul2.inputs[1])
    test_group.links.new(node_mul2.outputs[0], node_temp.inputs[0])

    ## link inputs
    test_group.links.new(group_inputs.outputs[0], node_rgb2bw.inputs[0])
    test_group.links.new(group_inputs.outputs[1], node_mul1.inputs[2])
    test_group.links.new(group_inputs.outputs[2], node_mul2.inputs[2])
    test_group.links.new(group_inputs.outputs[3], node_temp.inputs[1])
    test_group.links.new(group_inputs.outputs[4], node_temp.inputs[2])

    test_group.inputs[3].default_value = 1.533
    test_group.inputs[4].default_value = 1.353


    #glossinessFactorInput.min_value 
    #link output
    test_group.links.new(node_temp.outputs[0], group_outputs.inputs['Image'])
    return test_group

def Initiate(context):
    plane = bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.context.scene.use_nodes = True
    bpy.ops.transform.resize(value=(1.96046, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)   

    bpy.context.area.ui_type = 'CompositorNodeTree'
    global node1, node2, node3_1, node3_2, node3_3, node_ramp_1, node_ramp_2, node_bal, nodetree
    nodetree = bpy.context.scene.node_tree
    bpy.context.space_data.show_backdrop = True
    # adding Image node 1
   
    node1 = nodetree.nodes.new("CompositorNodeImage")
    node1.location = (100,200)

    #adding Viewer node 2
    node2 = nodetree.nodes.new("CompositorNodeViewer")
    node2.location = (1000,0)
    
    #adding ImageProcessing node 3
    node3_1 = nodetree.nodes.new(type='CompositorNodeGroup')
    node3_1.location = (700,300)
    node3_1.node_tree = create_V1('V1')

    node3_2 = nodetree.nodes.new(type='CompositorNodeGroup')
    node3_2.location = (700,0)
    node3_2.node_tree = create_V2('V2')

    node3_3 = nodetree.nodes.new(type='CompositorNodeGroup')
    node3_3.location = (700, -300)
    node3_3.node_tree = create_V3('V3')

    node_ramp_1 = nodetree.nodes.new('CompositorNodeValToRGB')
    node_ramp_1.location = (400, 0)
    node_ramp_1.color_ramp.elements[0].color = (0,0,0,1)
    node_ramp_1.color_ramp.elements[1].color = (1,1,1,1)
    node_ramp_1.color_ramp.elements[0].position = (0.029)
    node_ramp_1.color_ramp.elements[1].position = (0.069)

    node_ramp_2 = nodetree.nodes.new('CompositorNodeValToRGB')
    node_ramp_2.location = (400, -300)
    node_ramp_2.color_ramp.elements[0].color = (0,0,0,1)
    node_ramp_2.color_ramp.elements[1].color = (1,1,1,1)
    node_ramp_2.color_ramp.elements[0].position = (0.239)
    node_ramp_2.color_ramp.elements[1].position = (0.467)

    node_bal = nodetree.nodes.new('CompositorNodeColorBalance')
    node_bal.correction_method = 'LIFT_GAMMA_GAIN'
    node_bal.inputs[0].default_value = 0.9
    node_bal.lift = (1, 0.42, 0.0)
    node_bal.gamma = (1.1, 0.80, 1.1)
    node_bal.gain =  (1, 1, 1)
    node_bal.location = (400, -1000)

    #link Node
    #from image
    nodetree.links.new(node1.outputs["Image"],node3_1.inputs[0])
    nodetree.links.new(node1.outputs["Image"],node3_2.inputs[0])
    nodetree.links.new(node1.outputs["Image"],node3_3.inputs[0])
    nodetree.links.new(node1.outputs["Image"],node_ramp_1.inputs[0])
    nodetree.links.new(node1.outputs["Image"],node_ramp_2.inputs[0])
    nodetree.links.new(node1.outputs["Image"],node_bal.inputs[1])

    #from node
    nodetree.links.new(node_ramp_1.outputs["Image"],node3_2.inputs[1])
    nodetree.links.new(node_ramp_2.outputs["Image"],node3_3.inputs[1])
    nodetree.links.new(node_bal.outputs["Image"],node3_3.inputs[2])
    nodetree.links.new(node3_1.outputs["Image"],node2.inputs[0])


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Image Processing Addon"
    bl_idname = "IMAGE_PT_PROCESSING"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Image Processing Addon"
          
    def draw(self, context):     
        layout = self.layout
        scene = context.scene
        row = layout.row()
        row.operator("node.start",text="Start")
        layout.label(text="Import Image:")
        row = layout.row()
        row.prop(context.scene,'my_path')
        row.scale_y = 3.0
        row = layout.row()
        row.operator(SimpleOperator4.bl_idname)

        # Create a simple row.
        layout.label(text="Select Image Processing Version:")
        row = layout.row()
        row.operator("node.change_viwer1",text="์Normal Processing")
        row = layout.row()
        row.operator("node.change_viwer2",text="Low Bit Depth")
        row = layout.row()
        row.operator("node.change_viwer3",text="High Shadow")
        row = layout.row()

class Initiate_Program(bpy.types.Operator):
    bl_label = "Start Add-on"
    bl_idname = "node.start"
    def execute(self, context) :
        Initiate(context)
        return {'FINISHED'}

class HelloWorldPanel1(bpy.types.Panel):
    bl_idname = "HELLO_PT_World1"
    bl_label = "Version 1 Setting"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Image Processing Addon"
    def draw(self, context):
        layout = self.layout
        for index, item in enumerate(node3_1.inputs.values()):
            if index!=0 :
                row = layout.row()
                row.prop(node3_1.inputs[index], 'default_value', text=str(item.name))

class HelloWorldPanel2(bpy.types.Panel):
    bl_idname = "HELLO_PT_World2"
    bl_label = "Version 2 Setting"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Image Processing Addon"

    def draw(self, context):
        layout = self.layout
        for index, item in enumerate(node3_2.inputs.values()):
            if index!=0 and index>1:
                row = layout.row()
                row.prop(node3_2.inputs[index], 'default_value', text=str(item.name))
        layout.label(text="Pick White/Dark Space:")
        layout.template_color_ramp(node_ramp_1, "color_ramp", expand=True)
        
class HelloWorldPanel3(bpy.types.Panel):
    bl_idname = "HELLO_PT_World3"
    bl_label = "Version 3 Setting"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Image Processing Addon"
    def draw(self, context):
        layout = self.layout        
        for index, item in enumerate(node3_3.inputs.values()):
            if index!=0 and index>2:
                row = layout.row()
                row.prop(node3_3.inputs[index], 'default_value', text=str(item.name))
        layout.label(text="Pick White/Dark Space:")
        layout.template_color_ramp(node_ramp_2, "color_ramp", expand=True)
        
        row = layout.row()
        row.prop(context.scene, "color1")
        row.operator(SimpleOperator1.bl_idname)
        
        row = layout.row()
        row.prop(context.scene, "color2")
        row.operator(SimpleOperator2.bl_idname)
        
        row = layout.row()
        row.prop(context.scene, "color3")
        row.operator(SimpleOperator3.bl_idname)
        
class selected_viewer1(bpy.types.Operator):
    bl_label = "Change Viwer Node"
    bl_idname = "node.change_viwer1"
    def execute(self, context) :
        for i in bpy.data.images :
            print(i)
        nodetree.links.new(node3_1.outputs["Image"],node2.inputs[0])
        if hasattr(bpy.types, "HELLO_PT_World1") == False :
            bpy.utils.register_class(HelloWorldPanel1)
        if hasattr(bpy.types, "HELLO_PT_World2") == True:
            bpy.utils.unregister_class(HelloWorldPanel1)
        if hasattr(bpy.types, "HELLO_PT_World3") == True:
            bpy.utils.unregister_class(HelloWorldPanel3)
        node_bal.lift = (1, 1, 1 )
        node3_1.update()
        return {'FINISHED'}

class selected_viewer2(bpy.types.Operator):
    bl_label = "Change Viwer Node"
    bl_idname = "node.change_viwer2"
    def execute(self, context) :
        nodetree.links.new(node3_2.outputs["Image"],node2.inputs[0])
        if hasattr(bpy.types, "HELLO_PT_World2") == False :
            bpy.utils.register_class(HelloWorldPanel2)
        if hasattr(bpy.types, "HELLO_PT_World1") == True:
            bpy.utils.unregister_class(HelloWorldPanel1)
        if hasattr(bpy.types, "HELLO_PT_World3") == True:
            bpy.utils.unregister_class(HelloWorldPanel3)
        return {'FINISHED'}

class selected_viewer3(bpy.types.Operator):
    bl_label = "Change Viwer Node"
    bl_idname = "node.change_viwer3"
    def execute(self, context) :
        nodetree.links.new(node3_3.outputs["Image"],node2.inputs[0])
        if hasattr(bpy.types, "HELLO_PT_World3") == False:
            bpy.utils.register_class(HelloWorldPanel3)
        if hasattr(bpy.types, "HELLO_PT_World2") == True:
            bpy.utils.unregister_class(HelloWorldPanel2)
        if hasattr(bpy.types, "HELLO_PT_World1") == True:
            bpy.utils.unregister_class(HelloWorldPanel1)
        return {'FINISHED'}
    
class SimpleOperator1(bpy.types.Operator):
    bl_idname = "object.simple_operator1"
    bl_label = "Set"

    def execute(self, context):
        clr = context.scene.color1
        node_bal.lift = (clr[0], clr[1], clr[2])
        return {'FINISHED'}
    
class SimpleOperator2(bpy.types.Operator):
    bl_idname = "object.simple_operator2"
    bl_label = "Set"

    def execute(self, context):
        clr = context.scene.color2
        node_bal.gamma = (clr[0], clr[1], clr[2])
        return {'FINISHED'}

class SimpleOperator3(bpy.types.Operator):
    bl_idname = "object.simple_operator3"
    bl_label = "Set"

    def execute(self, context):
        clr = context.scene.color3
        node_bal.gain = (clr[0], clr[1], clr[2])
        return {'FINISHED'}

class SimpleOperator4(bpy.types.Operator):
    bl_idname = "object.simple_operator4"
    bl_label = "Set Image"
    def execute(self, context):
        clr = context.scene.my_path
        node1.image = bpy.data.images.load(clr)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(Initiate_Program)
    bpy.types.Scene.my_path = bpy.props.StringProperty(name='', subtype='FILE_PATH')
    bpy.utils.register_class(HelloWorldPanel1)
    bpy.utils.register_class(selected_viewer1)
    bpy.utils.register_class(selected_viewer2)
    bpy.utils.register_class(selected_viewer3)
    bpy.types.Scene.color1 = bpy.props.FloatVectorProperty(
                 name = "Set Shadows",
                 subtype = "COLOR",
                 size = 4,
                 min = 0.0,
                 max = 1.0,
                 default = (1.0, 0.5, 0.0, 0.5))
    bpy.types.Scene.color2 = bpy.props.FloatVectorProperty(
                 name = "Set Midtones",
                 subtype = "COLOR",
                 size = 4,
                 min = 0.0,
                 max = 1.0,
                 default = (1.0,0.6,0.9,0.5))
    bpy.types.Scene.color3 = bpy.props.FloatVectorProperty(
                 name = "Set Highlights",
                 subtype = "COLOR",
                 size = 4,
                 min = 0.0,
                 max = 1.0,
                 default = (1.0,1.0,1.0,0.5))
                 
    bpy.utils.register_class(SimpleOperator1)
    bpy.utils.register_class(SimpleOperator2)
    bpy.utils.register_class(SimpleOperator3)
    bpy.utils.register_class(SimpleOperator4)

def unregister():
    bpy.utils.unregister_class(Initiate_Program)
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.unregister_class(HelloWorldPanel1)
    bpy.utils.unregister_class(HelloWorldPanel2)
    bpy.utils.unregister_class(HelloWorldPanel3)
    bpy.utils.unregister_class(selected_viewer1)
    bpy.utils.unregister_class(selected_viewer2)
    bpy.utils.unregister_class(selected_viewer3)
    bpy.utils.unregister_class(SimpleOperator1)
    bpy.utils.unregister_class(SimpleOperator2)
    bpy.utils.unregister_class(SimpleOperator3)
    bpy.utils.unregister_class(SimpleOperator4)


if __name__ == "__main__":
    register()
