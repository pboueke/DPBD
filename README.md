# PDBD

## Creating the DB from backup:

```pg_restore --create --exit-on-error --verbose "path\to\file.backup"```

## Queries:

1. Selecionar todas as configurações (visc, dens, etc) após o programa EdgeCFD Pre referentes às malhas cavp.2, cavp.3 ou cavp.4 (mesh)

```SELECT "visc", "dens", "kxx", "kyy", "kzz", "mmodel" ```
```FROM "scc2-edgecfd"."oedgecfdpre" , "scc2-edgecfd"."dl_mat"```
```WHERE mesh = 'cavp.2' OR ```
```mesh = 'cavp.3' OR ```
```mesh = 'cavp.4' AND```
```"oedgecfdpre"."dl_matid" = "dl_mat"."id"```

[comment]: SELECT "visc", "dens", "kxx", "kyy", "kzz", "mmodel" FROM "scc2-edgecfd"."oedgecfdpre" , "scc2-edgecfd"."dl_mat" WHERE mesh = 'cavp.2' OR  mesh = 'cavp.3' OR  mesh = 'cavp.4' AND "oedgecfdpre"."dl_matid" = "dl_mat"."id" ORDER BY key ASC LIMIT 100

4. Selecionar todos os arquivos no formato dat (atributo dat) após a configuração das propriedades do solver (atividade SetSolverConfig) que utilizaram o algoritmo de solver (forcing) igual -4 ou -3

7. Selecionar a malha (atributo mesh), as propriedades do fluido (visc e dens) e o algoritmo do solver (forcing), em que a velocidade no eixo x (velocity_0) seja maior que 0.21
