#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This weeks debug challenge is fixing a monte-carlo simulation model.

The model is a simplification of a stroke treatment pathway at a hospital.  
Patients must be treated within 180 minutes of the onset of their symptoms.

* They must be brought to hospital
* be seen in the ED
* undego a CT scan
* be clinically assessed by a stroke medic
* not have any additional illnesses that prevent treatment

The model is implemented using a variety of distributions 
from numpy.random

The use of numpy reduces the need to sample using explicit 
`for` loops.  

The code currently does not run.  Can you fix it?


"""

import numpy as np
import math

class MonteCarloParameters(object):
    '''
    Class to holds the parameters for the
    monte-carlo simulation model 
    '''
    def __init__(self):
        pass


def normal_moments_from_lognormal(m, v):
    """
    Returns mu and sigma of normal distribution
    underlying a lognormal with mean m and variance v
    source: https://blogs.sas.com/content/iml/2014/06/04/simulate-lognormal-data-with-specified-mean-and-variance.html
    
    m -- mean of lognormal distribution
    v  variance of lognormal distribution
    """
    phi = math.sqrt(v + m**2)
    mu = math.log(m**2/phi)
    sigma = math.sqrt(math.log(phi**2/m**2))
    return mu, sigma


def gamma_parameters(mean, var):
    """
    Returns tuple with scale and shape of gamma distribution
    based on a mean and variance.
    
    Keyword arguments:
    mean -- mean of the gamma dist
    var -- variance of the gamma dist
    """
    scale = var / mean
    shape = var / (scale ** 2)
    return scale, shape
    


def results_summary(results):
    '''
    Display results
    Keyword arguments:
    results -- numpy.ndarray of weekly treatment percentages
    '''
    print('Weekly Treatment Rate')
    print('mean:\t\t{0:.3f}'.format(results.mean()))
    print('std err:\t{0:.3f}'.format(results.std() / math.sqrt(results.shape[0])))
    lower = np.percentile(results, 5)
    upper = np.percentile(results, 95)
    print('middle 90%:\t{0:.3f} - {1:.3f}'.format(lower, upper))
    


def sample_patients(params):
    '''
    Sample weekly no. of stroke patients
    Returns integer no. of patients 
    
    Keyword arguments:
    params - monte carlo parameters
    '''
    return np.random.poisson(params.mean_strokes)

def sample_ota(params, patients):
    '''
    Sample onset to arrival time 
    Return np.ndarray of samples (size = patients)
    
    Keyword arguments:
    params -- monte carlo parameters
    patients -- no. of samples to make
    
    '''
    return np.random.gamma(shape = params.onset_shape, 
                           scale = params.onset_scale, size = patients)
    

def sample_ed_delay(params, patients):
    '''
    Sample delay a patient experiences in the ED 
    Return np.ndarray of samples (size = patients)
    
    Keyword arguments:
    params -- monte carlo parameters
    patients -- no. of samples to make
    
    '''
    return np.random.lognormal(mean = params.mu_ed, 
                               sigma = params.sigma_ed, size = patients)
    

def sample_ct_scan(params, patients):
    '''
    Sample time it takes to undergo a CT scan and report results
    Return np.ndarray of samples (size = patients)
    
    Keyword arguments:
    params -- monte carlo parameters
    patients -- no. of samples to make
    
    '''
    return np.random.triangular(left = params.min_scan_time, 
                                mode = params.mode_scan_time, 
                                right = params.max_scan_time, size = patients)


def sample_assess_duration(params, patients):
    '''
    Sample the duration of clinical assessment
    Return np.ndarray of samples (size = patients)
    
    Keyword arguments:
    params -- monte carlo parameters
    patients -- no. of samples to make
    
    '''
    return np.random.uniform(low = params.min_assess_time, 
                             high = params.max_assess_time)
  


def eligible(patients, params):
    samples = np.random.uniform(0, 1, size = patients)
    return (samples >= 1 - params.p_contra_indication).sum()
            
            

def run_model(params, no_replications = 10000):
    '''
    Run the monte-carlo simulation
    
    Keyword arguments:
    params -- parameters for statistical distributions eg. mean and std
    no_replications -- no. indepedent replications (default = 10000)
    
    '''
    
    results = np.zeros(1000)

    
    for rep in range(no_replications):
    
        #number of patients with strokes in the week
        patients = sample_patients(params)
        
        #time taken from onset of stroke to arrival at a hospital
        ota = sample_ota(params, patients)
        
        #time taken for identificaion in the ED and alert of stroke team
        ed_delay = sample_ed_delay(params, patients)
        
        #time take to scan patient and report results
        ct_time = sample_ct_scan(params, patients)
        
        #time for stroke team to clinically assess patient
        assessment_time = sample_assess_duration(params, patients)

        #onset to treatment time for each patient (sum of numpy arrays)
        ott = ota + ed_delay + ct_time + assessment_time
        
        #patients in time
        patients_in_time = (ott < params.treatment_deadline).sum()
        
        #patients eligible for treatment
        results[rep] =  eligible(patients_in_time, params)

        # calculate percentage treated
        results[rep] /= patients 

    return results


        

def main():
    params = MonteCarloParameters() 
    
    #patients can only be treated if they are ready within 180 minutes
    params.treatment_deadline = 180
    
    #every 2/5 strokes  cannot have treatment due to other medical problems
    params.p_contra_indication = 0.4 
   
    #mean no. of strokes seen per week - poisson distribution
    params.mean_strokes = 12.5
   
    #onset to arrival time- gamma distribution
    mean_ota = 120
    std_ota = 60
    params.onset_scale, params.onset_shape = gamma_parameters(mean_ota, std_ota ** 2)
   
    #time in the emergency department - lognormal distribution
    params.mu_ed, params.sigma_ed = normal_moments_from_lognormal(60, 20)
   
    #time spent in CT scanner - triangular distribution
    params.min_scan_time = 15 
    params.mode_scan_time = 20
    params.max_scan_time = 30
   
    #eligibility assessment time by stroke physcian - uniform distribution
    params.min_assess_time = 5
    params.max_assess_time = 30
   
    
    results = run_model(params)
    
    results_summary(results)    


if __name__ == '__main__':
    main()


       
