from .models import Subject

def create_subj():
    sem_sub = {
    'SEM1': ['AM-I', 'AP-I', 'AC-I', 'EM', 'BEE', 'EVS'],
    'SEM2': ['AM-II', 'AP-II', 'AC-II', 'ED', 'SPA', 'CS'],
    'SEM3': ['AM-III', 'DLDA', 'DM', 'ECCF', 'DS'],
    'SEM4': ['AM-IV', 'AOA', 'COA', 'CG', 'OS'],
    'SEM5': ['MP', 'DBMS', 'CN', 'TCS', 'MS', 'AOS', 'AA'],
    'SEM6': ['SE', 'SPCC', 'DWM', 'CSS', 'ML', 'ADBMS', 'ERP', 'ACN'],
    'SEM7': ['DSIP', 'MCC', 'AI', 'ASSDF', 'BDA', 'ROB', 'PLM', 'RE', 'MIS', 'DE', 'OR', 'CSL', 'DMMM', 'EAM', 'DEVE'],
    'SEM8': ['HMI', 'DC', 'HPC', 'NLP', 'AWN', 'PM', 'FM', 'EDM', 'HRM', 'PECSR', 'RM', 'IPRP', 'DBM', 'ENM']
    }
    for sem in sem_sub:
        print(sem)
        for sub in sem_sub[sem]:
            print("sub: {} sem: {}".format(sem, sub))
            Subject.objects.get_or_create(sem=sem, name=sub)