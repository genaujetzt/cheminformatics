import pubchempy as pcp
import pandas as pd
wanted_CID = pd.read_csv("file:///home/vi/"
                         "Cheminformatics_MIPT/Practice/"
                         "A%5B0%5D/chem_id_pubmed.csv")
suffer = pcp.get_compounds(list(cids['459803']),'cid')
pcp.compounds_to_frame(suffer, properties=['isomeric_smiles', 'molecular_formula', 'fingerprint']).to_csv('homework1.csv')
