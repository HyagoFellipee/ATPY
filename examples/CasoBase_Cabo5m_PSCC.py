import card as crd 

card = crd.ATPCard() 

card.exact_phasor = True

# Miscellaneous

card.miscellaneous.delta_t = "1.E-11"
card.miscellaneous.t_max = "1.5E-6"


# Models

models = crd.Models()

models.add_inputs(["v(VL)", "v(VR)", "i(XX0006)", "v(VL2)", "v(VR2)", "i(XX0008)"])
models.add_outputs(["VLF", "VRF", "ILF", "VLF2", "VRF2", "ILF2"])
models.add_records(["VLF", "VRF", "ILF", "VLF2", "VRF2", "ILF2"])

model_code = crd.ModelCode()
model_code.name = "PBMOD"
model_code.add_code("code.txt")

model_box_bpfl1 = crd.ModelBox(model_code)
model_box_bpfl1.name = "BPFIL1"

model_box_bpfl1.inputs["X"] = "MM0003"
model_box_bpfl1.outputs["XF"] = "ILF"
model_box_bpfl1.datas = { 
    "Gain": "0.7425",
    "FilterFreq": "1.37E7",
    "FilterOrder": "2.",
    "ScaleFreq": "1.37E7"
}

model_box_bpfl2 = crd.ModelBox(model_code)
model_box_bpfl2.name = "BPFIL2"

model_box_bpfl2.inputs["X"] = "MM0001"
model_box_bpfl2.outputs["XF"] = "VLF"
model_box_bpfl2.datas = { 
    "Gain": "0.6931",
    "FilterFreq": "1.37E7",
    "FilterOrder": "2.",
    "ScaleFreq": "1.37E7"
}

model_box_bpfl3 = crd.ModelBox(model_code)
model_box_bpfl3.name = "BPFIL3"

model_box_bpfl3.inputs["X"] = "MM0002"
model_box_bpfl3.outputs["XF"] = "VRF"
model_box_bpfl3.datas = { 
    "Gain": "0.7425",
    "FilterFreq": "1.37E7",
    "FilterOrder": "2.",
    "ScaleFreq": "1.37E7"
}

model_box_bpfl4 = crd.ModelBox(model_code)
model_box_bpfl4.name = "BPFIL4"

model_box_bpfl4.inputs["X"] = "MM0006"
model_box_bpfl4.outputs["XF"] = "ILF2"
model_box_bpfl4.datas = { 
    "Gain": "0.782813",
    "FilterFreq": "1.37E7",
    "FilterOrder": "2.",
    "ScaleFreq": "1.37E7"
}

model_box_bpfl5 = crd.ModelBox(model_code)
model_box_bpfl5.name = "BPFIL5"

model_box_bpfl5.inputs["X"] = "MM0004"
model_box_bpfl5.outputs["XF"] = "VLF2"
model_box_bpfl5.datas = { 
    "Gain": "0.6931",
    "FilterFreq": "1.37E7",
    "FilterOrder": "2.",
    "ScaleFreq": "1.37E7"
}

model_box_bpfl6 = crd.ModelBox(model_code)
model_box_bpfl6.name = "BPFIL6"

model_box_bpfl6.inputs["X"] = "MM0005"
model_box_bpfl6.outputs["XF"] = "VRF2"
model_box_bpfl6.datas = { 
    "Gain": "0.7425",
    "FilterFreq": "1.37E7",
    "FilterOrder": "2.",
    "ScaleFreq": "1.37E7"
}

models.model_boxes = [model_box_bpfl2, model_box_bpfl3, model_box_bpfl1, model_box_bpfl5, model_box_bpfl6, model_box_bpfl4]
models.models_codes = [model_code]

card.models = models

# BRANCHES

branches = crd.Branch()

rlc_dist1 = crd.RlcElementDistParams()
rlc_dist1.line = "-1VL    XX0002            .0705857.3192.18E8   2.5 1 1                         0"
rlc_dist2 = crd.RlcElementDistParams()
rlc_dist2.line = "-1XX0002VR                .0705857.3192.18E8   2.5 1 1                         0"
rlc_dist3 = crd.RlcElementDistParams()
rlc_dist3.line = "-1VL2   XX0004            .0705857.3192.18E8   2.5 1 1                         0"
rlc_dist4 = crd.RlcElementDistParams()
rlc_dist4.line = "-1XX0004VR2               .0705857.3192.18E8   2.5 1 1                         0"

rlc_basic1 = crd.RlcElementBasic()
rlc_basic1.line = "  VL                        1.E7                                               0"
rlc_basic2 = crd.RlcElementBasic()
rlc_basic2.line = "  VR                        1.E7                                               0"
rlc_basic3 = crd.RlcElementBasic()
rlc_basic3.line = "  XX0005XX0001               25.                                               0"
rlc_basic4 = crd.RlcElementBasic()
rlc_basic4.line = "  VL2                       1.E7                                               0"
rlc_basic5 = crd.RlcElementBasic()
rlc_basic5.line = "  VR2                       1.E7                                               0"
rlc_basic6 = crd.RlcElementBasic()
rlc_basic6.line = "  XX0007XX0003               25.                                               0"
rlc_basic7 = crd.RlcElementBasic()
rlc_basic7.line = "  XX0003                      1.                                               0"

branches.branches = [rlc_dist1, rlc_basic1, rlc_basic2, rlc_dist2, rlc_basic3, rlc_dist3, rlc_basic4, rlc_basic5, rlc_dist4, rlc_basic6, rlc_basic7]

card.branch = branches

# SWITCHES

switches = crd.Switch()

switch_1 = crd.SwitchElement()
switch_1.line = "  XX0001XX0006                                        MEASURING                "
switch_2 = crd.SwitchElement()
switch_2.line = "  XX0006VL                                            MEASURING                1"
switch_3 = crd.SwitchElement()
switch_3.line = "  XX0003XX0008                                        MEASURING                "
switch_4 = crd.SwitchElement()
switch_4.line = "  XX0008VL2                                           MEASURING                1"

switches.switches = [switch_1, switch_2, switch_3, switch_4]

card.switch = switches

# SOURCES   

sources = crd.Source()

source_heidler1 = crd.HeidlerSource()
source_heidler1.line = "15XX0005 0        2.     2.E-8      100.        2.              6.5E-8      1.E3"

source_heidler2 = source_heidler1
source_heidler1.name = "XX0007"


sources.sources = [source_heidler1, source_heidler2]

card.source = sources

# OUTPUTS

outputs = crd.Output()
outputs.add_vars(["VR", "VL", "VR2", "VL2"])
card.output = outputs

print(outputs.vars)

card.write_to_file("CasoBase_Cabo5m_PSCC_gerado.atp")