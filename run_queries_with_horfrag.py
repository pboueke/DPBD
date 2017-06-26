import psycopg2
import time

q1 = """SELECT DISTINCT "visc", "dens", "kxx", "kyy", "kzz", "mmodel",  "mesh" FROM "scc2-edgecfd"."oedgecfdpre_234" , "scc2-edgecfd"."dl_mat" WHERE "oedgecfdpre_234"."dl_matid" = "dl_mat"."rid" """

q2 = """SELECT DISTINCT dat FROM "scc2-edgecfd".osetsolverconfig, "scc2-edgecfd".dl_in_n3n4, "scc2-edgecfd".oedgecfdpre WHERE osetsolverconfig.previoustaskid = oedgecfdpre.nexttaskid  AND dl_in_n3n4.rid = oedgecfdpre.dl_inid"""

q3 = """SELECT DISTINCT oedgecfdsolver.mesh, visc, dens, forcing FROM "scc2-edgecfd".dl_in, "scc2-edgecfd".dl_mat, "scc2-edgecfd".dl_solver_gt021, "scc2-edgecfd".oedgecfdpre,"scc2-edgecfd".osetsolverconfig, "scc2-edgecfd".oedgecfdsolver WHERE dl_solver_gt021.rid = oedgecfdsolver.dl_solverid AND oedgecfdsolver.taskid = osetsolverconfig.nexttaskid AND osetsolverconfig.previoustaskid = oedgecfdpre.nexttaskid AND oedgecfdpre.dl_matid = dl_mat.rid AND oedgecfdpre.dl_inid = dl_in.rid"""

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
