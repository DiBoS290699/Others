from gatspy import datasets, periodic
rrlyrae = datasets.fetch_rrlyrae()
lcid = rrlyrae.ids[0]
t, mag, dmag, filts = rrlyrae.get_lightcurve(lcid)
mask = (filts == 'r')
t_r, mag_r, dmag_r = t[mask], mag[mask], dmag[mask]
model = periodic.LombScargleFast(fit_period=True)
model.optimizer.period_range = (0.2, 1.2)
model.fit(t_r, mag_r, dmag_r)
print(model.best_period)
metadata = rrlyrae.get_metadata(lcid)
true_period = metadata['P']
print(true_period)
import numpy as np
tfit = np.linspace(0, model.best_period, 4)
print(model.predict(tfit))
model = periodic.LombScargleFast(fit_period=True)
model.optimizer.period_range = (0.2, 1.2)
model.fit(t_r, mag_r, dmag_r)
print(model.best_period)
model = periodic.LombScargleFast(fit_period=True)
model.optimizer.set(period_range=(0.5, 0.7), first_pass_coverage=10)
model.fit(t_r, mag_r, dmag_r)
print(model.best_period)