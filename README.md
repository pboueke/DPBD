# PDBD

## Criando banco a partir do backup:

```pg_restore --create --exit-on-error --verbose "path\to\file.backup"```

## Queries:

1) Selecionar todas as configurações (visc, dens, etc) após o programa EdgeCFD Pre referentes às malhas cavp.2, cavp.3 ou cavp.4 (mesh)

```SELECT DISTINCT "visc", "dens", "kxx", "kyy", "kzz", "mmodel", "mesh" ```
```FROM "scc2-edgecfd"."oedgecfdpre" , "scc2-edgecfd"."dl_mat"```
```WHERE mesh = 'cavp.2' OR ```
```mesh = 'cavp.3' OR ```
```mesh = 'cavp.4' AND```
```"oedgecfdpre"."dl_matid" = "dl_mat"."rid"```

* **Tempo real: ** 0.007s

[comment]: SELECT DISTINCT "visc", "dens", "kxx", "kyy", "kzz", "mmodel",  "mesh" FROM "scc2-edgecfd"."oedgecfdpre" , "scc2-edgecfd"."dl_mat" WHERE mesh = 'cavp.2' OR  mesh = 'cavp.3' OR  mesh = 'cavp.4' AND "oedgecfdpre"."dl_matid" = "dl_mat"."rid"

4)  Selecionar todos os arquivos no formato dat (atributo dat) após a configuração das propriedades do solver (atividade SetSolverConfig) que utilizaram o algoritmo de solver (forcing) igual -4 ou -3

```SELECT DISTINCT dat ```
```FROM "scc2-edgecfd".osetsolverconfig, "scc2-edgecfd".dl_in, "scc2-edgecfd".oedgecfdpre```
```WHERE osetsolverconfig.previoustaskid = oedgecfdpre.nexttaskid ```
```AND dl_in.rid = oedgecfdpre.dl_inid ```
```AND dl_in.forcing in (-3, -4) ```

* **Tempo real: ** 0.002s

[comment]: SELECT DISTINCT dat
FROM "scc2-edgecfd".osetsolverconfig, "scc2-edgecfd".dl_in, "scc2-edgecfd".oedgecfdpre WHERE osetsolverconfig.previoustaskid = oedgecfdpre.nexttaskid  AND dl_in.rid = oedgecfdpre.dl_inid  AND dl_in.forcing in (-3, -4)

7) Selecionar a malha (atributo mesh), as propriedades do fluido (visc e dens) e o algoritmo do solver (forcing), em que a velocidade no eixo x (velocity_0) seja maior que 0.21

```SELECT DISTINCT oedgecfdsolver.mesh, visc, dens, forcing```
```FROM "scc2-edgecfd".dl_in, "scc2-edgecfd".dl_mat, "scc2-edgecfd".dl_solver, "scc2-edgecfd".oedgecfdpre,"scc2-edgecfd".osetsolverconfig, "scc2-edgecfd".oedgecfdsolver```
```WHERE dl_solver.rid = oedgecfdsolver.dl_solverid```
```AND oedgecfdsolver.taskid = osetsolverconfig.nexttaskid```
```AND osetsolverconfig.previoustaskid = oedgecfdpre.nexttaskid```
```AND oedgecfdpre.dl_matid = dl_mat.rid```
```AND oedgecfdpre.dl_inid = dl_in.rid```
```AND dl_solver.velocity_0 > 0.21```

* **Tempo real: ** 0.163s

[comment]: SELECT DISTINCT oedgecfdsolver.mesh, visc, dens, forcing FROM "scc2-edgecfd".dl_in, "scc2-edgecfd".dl_mat, "scc2-edgecfd".dl_solver, "scc2-edgecfd".oedgecfdpre,"scc2-edgecfd".osetsolverconfig, "scc2-edgecfd".oedgecfdsolver WHERE dl_solver.rid = oedgecfdsolver.dl_solverid AND oedgecfdsolver.taskid = osetsolverconfig.nexttaskid AND osetsolverconfig.previoustaskid = oedgecfdpre.nexttaskid AND oedgecfdpre.dl_matid = dl_mat.rid AND oedgecfdpre.dl_inid = dl_in.rid AND dl_solver.velocity_0 > 0.21

![queries](img/schema.png)

## Propostas de Fragmentação

### Fragmentação Horizontal
