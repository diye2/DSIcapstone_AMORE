from read_input import read_eqns, read_spc, read_def
path = 'isoprene_oxidation_model_v5_190415'
eqn_file = path+'/isoprene_full_v5.eqn'
spc_file = path+'/isoprene_full_v5.spc'
def_file = path+'/isoprene_full_v5.def'
equations = read_eqns(eqn_file)
species = read_spc(spc_file)
inits = read_def(def_file)

from calculations import calculate_weight
eqn = equations[0]
calculate_weight(eqn, inits)
