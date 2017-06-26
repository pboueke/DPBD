import psycopg2
import time

q1 = """SELECT "visc", "dens", "kxx", "kyy", "kzz", "mmodel" """
q1 += """FROM "scc2-edgecfd"."oedgecfdpre" , "scc2-edgecfd"."dl_mat" """
q1 += """WHERE mesh = 'cavp.2' OR  mesh = 'cavp.3' OR  mesh = 'cavp.4' AND "oedgecfdpre"."dl_matid" = "dl_mat"."id" """

q2 = """SELECT DISTINCT dat """
q2 += """FROM "scc2-edgecfd".osetsolverconfig, "scc2-edgecfd".dl_in, "scc2-edgecfd".dl_pre,  "scc2-edgecfd".oedgecfdpre """
q2 += """WHERE osetsolverconfig.dl_preid = oedgecfdpre.dl_preid AND dl_in.id = oedgecfdpre.dl_inid AND dl_in.forcing in (-3, -4)"""

q3 =  """SELECT DISTINCT oedgecfdsolver.mesh, visc, dens, forcing """
q3 += """FROM "scc2-edgecfd".dl_in, "scc2-edgecfd".dl_mat, "scc2-edgecfd".dl_solver, "scc2-edgecfd".oedgecfdpre, "scc2-edgecfd".oedgecfdsolver """
q3 += """WHERE dl_solver.rid = oedgecfdsolver.dl_solverid AND oedgecfdsolver.ewkfid = oedgecfdpre.ewkfid AND oedgecfdpre.dl_matid = dl_mat.id AND oedgecfdpre.dl_inid = dl_in.id AND dl_solver.velocity_0 > 0.21"""

print ("Connecting to DB...")
conn = psycopg2.connect("dbname=edgecfd-program-p user=postgres password=1337jawaftw")
cur = conn.cursor()

print ("Executing query #1...")
starttime = time.time()
cur.execute(q1)
print(time.time() - starttime)

print ("Executing query #2...")
starttime = time.time()
cur.execute(q2)
print(time.time() - starttime)

print ("Executing query #3...")
starttime = time.time()
cur.execute(q3)
print(time.time() - starttime)

print ("")
input("All Done.")
