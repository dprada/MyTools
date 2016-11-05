import pyemma

def most_weighted_node_in_basin(basin,pcca):
    jj=pcca.stationary_probability[pcca.metastable_sets[basin]].argmax()
    jj=pcca.metastable_sets[basin][jj]
    return jj

def most_weighted_node(nodes,pcca):
    jj=pcca.stationary_probability[nodes].argmax()
    jj=nodes[jj]
    return jj

def translate_tptsets2originalnodes(list_sets,tpt_sets):
    aux_list=[]
    for ii in list_sets:
        aux_list+=list(tpt_sets[ii])
    return aux_list

