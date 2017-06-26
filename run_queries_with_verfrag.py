import psycopg2
import time

q1 = """SELECT DISTINCT "visc", "dens" FROM "scc2-edgecfd"."oedgecfdpre_sq4" , "scc2-edgecfd"."dl_mat_sq1" WHERE mesh = 'cavp.2' OR  mesh = 'cavp.3' OR  mesh = 'cavp.4' AND "oedgecfdpre_sq4"."dl_matid" = "dl_mat_sq1"."rid" """

q2 = """SELECT DISTINCT dat FROM "scc2-edgecfd".osetsolverconfig, "scc2-edgecfd".dl_in, "scc2-edgecfd".oedgecfdpre_sq4 WHERE osetsolverconfig.previoustaskid = oedgecfdpre_sq4.nexttaskid  AND dl_in.rid = oedgecfdpre_sq4.dl_inid  AND dl_in.forcing in (-3, -4)"""

q3 = """SELECT DISTINCT oedgecfdsolver.mesh, visc, dens, forcing FROM "scc2-edgecfd".dl_in, "scc2-edgecfd".dl_mat_sq1, "scc2-edgecfd".dl_solver_sq7, "scc2-edgecfd".oedgecfdpre_sq4,"scc2-edgecfd".osetsolverconfig, "scc2-edgecfd".oedgecfdsolver WHERE dl_solver_sq7.rid = oedgecfdsolver.dl_solverid AND oedgecfdsolver.taskid = osetsolverconfig.nexttaskid AND osetsolverconfig.previoustaskid = oedgecfdpre_sq4.nexttaskid AND oedgecfdpre_sq4.dl_matid = dl_mat_sq1.rid AND oedgecfdpre_sq4.dl_inid = dl_in.rid AND dl_solver_sq7.velocity_0 >  0.21"""

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
