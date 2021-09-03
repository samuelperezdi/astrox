# Documentación 

## Clusterización con K-means para diferentes números de clusters y características

---

This clustering was done by ignoring 0 values in the logarithmic transformations done for several descriptors. Also, the clusters are not the same in each clusterization.

**1. **`astrox_knn6_var.csv`
Se realiza una clusterización con $$k=6$$ para los siguientes descriptores:

   ```
   'hard_hm','hard_hs', 'hard_ms', 'var_prob_b', 'var_sigma_b',
   'var_prob_h', 'var_sigma_h','var_prob_m', 'var_sigma_m', 'var_prob_s', 'var_sigma_s', 'ks_prob_b','ks_prob_h','ks_prob_m', 'ks_prob_s', 'kp_prob_b', 'kp_prob_h', 'kp_prob_m','kp_prob_s'
   ```

   Se le realiza transformación logarítmica y posterior normalización a los siguientes descriptores:
      ```
     'var_sigma_b', 'var_sigma_h', 'var_sigma_m', 'var_sigma_s'
      ```

   **Visualización de los clusters:**
   ![](img/astrox_knn6_var.png)

---

**2.** `astrox_knn3_var.csv`
Se realiza un procedimiento análogo al anterior, con la variación de que ahora tenemos una clusterización con $$k=3$$.

   **Visualización de los clusters:**
   ![](img/astrox_knn3_var.png)

---

**3.** `astrox_knn9_src.csv`
Se realiza una clusterización con $$k=9$$ para los siguientes descriptores (los mismos de los anteriores casos, agregando `'src_area_b'` y `'bb_kt'`)

   ```
'src_area_b', 'hard_hm', 'hard_hs', 'hard_ms', 'var_prob_b', 'var_sigma_b', 'var_prob_h', 'var_sigma_h', 'var_prob_m', 'var_sigma_m', 'var_prob_s', 'var_sigma_s', 'ks_prob_b', 'ks_prob_h','ks_prob_m', 'ks_prob_s', 'kp_prob_b', 'kp_prob_h', 'kp_prob_m','kp_prob_s', 'bb_kt'
   ```

   Se le realiza transformación logarítmica y posterior normalización a los siguientes descriptores:
      ```
     'var_sigma_b', 'var_sigma_h', 'var_sigma_m', 'var_sigma_s', 'src_area_b', 'bb_kt'
      ```

   **Visualización de los clusters:**
   ![](img/astrox_knn9_src.png)

---

**4.** `astrox_knn6_src.csv`

Se realiza un procedimiento análogo al anterior, con la variación de que ahora tenemos una clusterización con $$k=6$$.

   **Visualización de los clusters:**
   ![](img/astrox_knn6_src.png)

---

**4.** `astrox_knn3_src.csv`

Se realiza un procedimiento análogo al anterior, con la variación de que ahora tenemos una clusterización con $$k=3$$.

   **Visualización de los clusters:**

![](img/astrox_knn3_src.png)