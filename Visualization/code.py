# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts()
loan_status.plot(kind='bar')
plt.title('Loan_Status visualized')
plt.xlabel('Loan_status')
plt.ylabel('Total Customers')
plt.legend(labels=['Yes','No'])
plt.show()


#Code starts here


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)

property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()

property_and_loan.plot(kind='bar',stacked=False)

plt.xlabel('Property Area')

plt.ylabel('Loan Status')

plt.xticks(rotation=45)


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)

education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()

education_and_loan.plot(kind='bar',stacked=True)

plt.xlabel('Education Status')

plt.ylabel('Loan Status')

plt.xticks(rotation=45)


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)

graduate=data[data['Education'] == 'Graduate']

not_graduate=data[data['Education']=='Not Graduate']

graduate['LoanAmount'].value_counts().plot(kind='density',label='Graduate')

not_graduate['LoanAmount'].value_counts().plot(kind='density',label='Not Graduate')


#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(15,15))

data=pd.read_csv(path)

data.plot.scatter(x='ApplicantIncome',y='LoanAmount',ax=ax_1,)
plt.title('Applicant Income')

data.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
plt.title('Coapplicant Income')

data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome',y='LoanAmount',ax=ax_3)
plt.title('Total Income')


