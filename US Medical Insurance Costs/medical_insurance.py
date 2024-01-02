# The CSV library is introdued in order to manipulate csv data into lists for easier analysis in Python
import csv

# As per the data initialized in the file, we define the individual lists for each fieldname
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []


# To initialize the ease of use for data analysis we define a function that will take in the csv file and create a set of lists according to their fieldnames:
def data_segregation(field_list, csv_file, row_header):

    # Initialize opening of the csv file as a reader object
    with open(csv_file) as reader_file:
        data_file = csv.DictReader(reader_file)
        
        #With the DictReader object, loop each row to append to the designated list
        for row in data_file:
            field_list.append(row[row_header])
        
        # return the updated list
        return field_list

# Let's update each individual list
data_segregation(age, 'insurance.csv', 'age')
data_segregation(sex, 'insurance.csv', 'sex')
data_segregation(bmi, 'insurance.csv', 'bmi')
data_segregation(children, 'insurance.csv', 'children')
data_segregation(smoker, 'insurance.csv', 'smoker')
data_segregation(region, 'insurance.csv', 'region')
data_segregation(charges, 'insurance.csv', 'charges')

# Review the list elements to check for data consistency
# print(age)
# print(bmi)
# print(sex)

# To analyze patient's data, the following objectives have been defined:
# 1. Identify the average age of patients
# 2. The Total proportion of Males vs. Females in the dataset
# 3. The geographic location of the patients
# 4. Average yearly charges of the patients
# 5. Creating a dictionary that contains each patient's data

# To modularize each code element, a class is defined to contain the methods for the above tasks

class InsuranceData:
    # Constructor to define the incoming parameters and each list data
    def __init__(self, patient_age, patient_sex, patient_bmi, patient_num_children, patient_smoker, patient_region, patient_charge):
        self.patient_age = patient_age
        self.patient_sex = patient_sex
        self.patient_bmi = patient_bmi
        self.patient_num_children = patient_num_children
        self.patient_smoker = patient_smoker
        self.patient_region = patient_region
        self.patient_charge = patient_charge

    # 1. Average age calculation method
    def average_age(self):
        # Initialize overall age
        overall_age = 0
        # add all ages to variable from list through iteration
        for age in self.patient_age:
            overall_age += int(age)
        
        # Return average by calculating overall_age divided by length of patient list
            
        aggregated_age = round(overall_age / len(self.patient_age), 1)

        return "Average Insurer age is {0} years".format(aggregated_age)
    
    # 2. Proportion of Males and Females in the dataset
    def sex_proportion(self):
        # Counters to identify total counter of male to females in the dataset
        
        male_counter = self.patient_sex.count('male')
        
        female_counter = self.patient_sex.count('female')
        
        # To Calculate the proportions, we divide each counter against the total size of the dataset

        male_proportion = male_counter / len(self.patient_sex)
        female_proportion = female_counter / len(self.patient_sex)
        
        # To Convert floats to % format we use the str.format() method
        male_pct = "{:.2%}".format(male_proportion)
        female_pct = "{:.2%}".format(female_proportion)

        print(male_counter, female_counter)
        return 'Males account for {0} of the dataset, where Females account for {1} of the dataset'.format(male_pct, female_pct)
    
    #3. Defining the geographic areas of the dataset
    def region_coverage(self):
        # Each unique region to be added in a list
        regions = []

        # Loop over region list and append those that do not exists in the unique region list

        for region in self.patient_region:
            if not region in regions:
                regions.append(region)
        
        return regions


    #4. Average yearly charges
    def charges_difference(self):
        # Variables to add onto cost
        total_charges = 0

        for cost in self.patient_charge:
            total_charges += float(cost)
        
        average_charge = round(total_charges / len(self.patient_charge), 2)

        return "Average yearly insurance charge Medical Insurance Charges: {0} dollars.".format(average_charge)

    #5. Create Dictionary that includes each patient's data point
    def insurance_dictionary(self):
        self.patient_dictionary = {}
        
        self.patient_dictionary['age'] = [int(age) for age in self.patient_age]
        self.patient_dictionary['sex'] = self.patient_sex
        self.patient_dictionary['bmi'] = self.patient_bmi
        self.patient_dictionary['children'] = self.patient_num_children
        self.patient_dictionary['smoker'] = self.patient_smoker
        self.patient_dictionary['charges'] = self.patient_charge
    
        return self.patient_dictionary




insurer_info = InsuranceData(age, sex, bmi, children, smoker, region, charges)

print(insurer_info.average_age())
print(insurer_info.sex_proportion())
print(insurer_info.region_coverage())
print(insurer_info.charges_difference())
print(insurer_info.insurance_dictionary())
