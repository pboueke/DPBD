# PDBD

## Criando banco a partir do backup:

```pg_restore --create --exit-on-error --verbose "path\to\file.backup"```

## Queries:

1) Selecionar todas as configurações (visc, dens, etc) após o programa EdgeCFD Pre referentes às malhas cavp.2, cavp.3 ou cavp.4 (mesh)

```SELECT "visc", "dens", "kxx", "kyy", "kzz", "mmodel" ```
```FROM "scc2-edgecfd"."oedgecfdpre" , "scc2-edgecfd"."dl_mat"```
```WHERE mesh = 'cavp.2' OR ```
```mesh = 'cavp.3' OR ```
```mesh = 'cavp.4' AND```
```"oedgecfdpre"."dl_matid" = "dl_mat"."id"```

* **Tempo real: ** 0.025s

[comment]: SELECT "visc", "dens", "kxx", "kyy", "kzz", "mmodel" FROM "scc2-edgecfd"."oedgecfdpre" , "scc2-edgecfd"."dl_mat" WHERE mesh = 'cavp.2' OR  mesh = 'cavp.3' OR  mesh = 'cavp.4' AND "oedgecfdpre"."dl_matid" = "dl_mat"."id" ORDER BY key ASC LIMIT 100

4)  Selecionar todos os arquivos no formato dat (atributo dat) após a configuração das propriedades do solver (atividade SetSolverConfig) que utilizaram o algoritmo de solver (forcing) igual -4 ou -3

```SELECT DISTINCT dat FROM "scc2-edgecfd".osetsolverconfig, "scc2-edgecfd".dl_in,  "scc2-edgecfd".oedgecfdpre```
```WHERE osetsolverconfig.dl_preid = oedgecfdpre.dl_preid AND```
```dl_in.id = oedgecfdpre.dl_inid AND```
```dl_in.forcing in (-3, -4)```

* **Tempo real: ** 0.010s

[comment]: SELECT DISTINCT dat FROM "scc2-edgecfd".osetsolverconfig, "scc2-edgecfd".dl_in, "scc2-edgecfd".dl_pre,  "scc2-edgecfd".oedgecfdpre WHERE osetsolverconfig.dl_preid = oedgecfdpre.dl_preid AND dl_in.id = oedgecfdpre.dl_inid AND dl_in.forcing in (-3, -4) LIMIT 100

7) Selecionar a malha (atributo mesh), as propriedades do fluido (visc e dens) e o algoritmo do solver (forcing), em que a velocidade no eixo x (velocity_0) seja maior que 0.21

```SELECT DISTINCT oedgecfdsolver.mesh, visc, dens, forcing```
```FROM "scc2-edgecfd".dl_in, "scc2-edgecfd".dl_mat, "scc2-edgecfd".dl_solver, "scc2-edgecfd".oedgecfdpre, "scc2-edgecfd".oedgecfdsolver```
```WHERE dl_solver.rid = oedgecfdsolver.dl_solverid```
```AND oedgecfdsolver.ewkfid = oedgecfdpre.ewkfid```
```AND oedgecfdpre.dl_matid = dl_mat.id```
```AND oedgecfdpre.dl_inid = dl_in.id```
```AND dl_solver.velocity_0 > 0.21```

* **Tempo real: ** 19.118s

[comment]: SELECT DISTINCT oedgecfdsolver.mesh, visc, dens, forcing FROM "scc2-edgecfd".dl_in, "scc2-edgecfd".dl_mat, "scc2-edgecfd".dl_solver, "scc2-edgecfd".oedgecfdpre, "scc2-edgecfd".oedgecfdsolver WHERE dl_solver.rid = oedgecfdsolver.dl_solverid AND oedgecfdsolver.ewkfid = oedgecfdpre.ewkfid AND oedgecfdpre.dl_matid = dl_mat.id AND oedgecfdpre.dl_inid = dl_in.id AND dl_solver.velocity_0 > 0.21

![queries](img/schema.png)

## Propostas de Fragmentação

### Fragmentação Horizontal
