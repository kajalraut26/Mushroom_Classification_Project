#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.ensemble import RandomForestClassifier


# In[33]:


st.title('Predicting Mushroom Type')


# In[34]:


st.subheader('Enter Parameters')


# In[35]:


def user_input_features():
    
    Cap_Shape= st.selectbox('Cap Shape',('Bell','Conical','Convex','Flat', 'Knobbed','Sunken'))
    if Cap_Shape=='Bell':
        Cap_Shape=0
    elif Cap_Shape=='Conical':
        Cap_Shape=1
    elif Cap_Shape=='Convex':
        Cap_Shape=5
    elif Cap_Shape=='Flat':
        Cap_Shape=2
    elif Cap_Shape=='Knobbed':
        Cap_Shape=3
    else:
        Cap_Shape=4


    Cap_Surface= st.selectbox('Cap Surface',('Fibrous','Grooves','Scaly','Smooth'))
    if Cap_Surface=='Fibrous':
        Cap_Surface=0
    elif Cap_Surface=='Grooves':
        Cap_Surface=1
    elif Cap_Surface=='Scaly':
        Cap_Surface=3
    else:
        Cap_Surfacee=2

        
    Cap_Color= st.selectbox('Cap Color',('Brown','Buff','Cinnamon','Gray','Green','Pink','Purple','Red','White','Yellow'))
    if Cap_Color=='Brown':
        Cap_Color=4
    elif Cap_Color=='Buff':
        Cap_Color=0
    elif Cap_Color=='Cinnamon':
        Cap_Color=1
    elif Cap_Color=='Gray':
        Cap_Color=3
    elif Cap_Color=='Green':
        Cap_Color=6
    elif Cap_Color=='Pink':
        Cap_Color=5
    elif Cap_Color=='Purple':
        Cap_Color=7
    elif Cap_Color=='Red':
        Cap_Color=2
    elif Cap_Color=='White':
        Cap_Color=8
    else:
        Cap_Color=9
        
    
    Bruises= st.selectbox('Bruises',('Present','Absent'))
    if Bruises=='Present':
        Bruises=1
    else:
        Bruises=0

        
    Odor= st.selectbox('Odor',('Almond','Anise','Creosote','Fishy','Foul','Musty','None','Pungent','Spicy'))
    if Odor=='Almond':
        Odor=0
    elif Odor == 'Anise':
        Odor=3
    elif Odor == 'Creosote':
        Odor=1
    elif Odor == 'Fishy':
        Odor=8
    elif Odor == 'Foul':
        Odor=2
    elif Odor == 'Musty':
        Odor=4
    elif Odor == 'None':
        Odor=5
    elif Odor == 'Pungent':
        Odor=6
    else:
        Odor=7
        
        
    Gill_Spacing=st.selectbox('Gill Spacing',('Close','Crowded','Distant'))
    if Gill_Spacing=='Close':
        Gill_Spacing=0
    elif Gill_Spacing=='Crowded':
        Gill_Spacing=2
    else:
        Gill_Spacing=1
        
    
    Gill_Size=st.selectbox('Gill Size',('Broad','Narrow'))
    if Gill_Size=='Broad':
        Gill_Size=0
    else:
        Gill_Size=1
        
        
    Gill_Color=st.selectbox('Gill Color',('Black','Brown','Buff','Chocolate','Gray','Green','Orange','Pink','Purple','Red','White','Yellow'))
    if Gill_Color=='Black':
        Gill_Color=4
    elif Gill_Color=='Brown':
        Gill_Color=5
    elif Gill_Color=='Buff':
        Gill_Color=0
    elif Gill_Color=='Chocolate':
        Gill_Color=3
    elif Gill_Color=='Gray':
        Gill_Color=2
    elif Gill_Color=='Green':
        Gill_Color=8
    elif Gill_Color=='Orange':
        Gill_Color=6
    elif Gill_Color=='Pink':
        Gill_Color=7
    elif Gill_Color=='Purple':
        Gill_Color=9
    elif Gill_Color=='Red':
        Gill_Color=1
    elif Gill_Color=='White':
        Gill_Color=10
    else:
        Gill_Color=11
        
    
    Stalk_Shape= st.selectbox('Stalk Shape',('Enlarging','Tapering'))
    if Stalk_Shape=='Enlarging':
        Stalk_Shape=0
    else:
        Stalk_Shape=1
    
    
    Stalk_Root= st.selectbox('Stalk Root',('Bulbous','Club','Cup','Equal','Rhizomorphs','Rooted','Unknown'))
    if Stalk_Root=='Bulbous':
        Stalk_Root=1
    elif Stalk_Root=='Club':
        Stalk_Root=2
    elif Stalk_Root=='Cup':
        Stalk_Root=5
    elif Stalk_Root=='Equal':
        Stalk_Root=3
    elif Stalk_Root=='Rhizomorphs':
        Stalk_Root=6
    elif Stalk_Root=='Rooted':
        Stalk_Root=4
    else:
        Stalk_Root=0
    
    
    Stalk_Surface_Above_Ring= st.selectbox('Stalk Surface Above Ring',('Fibrous','Scaly','Silky','Smooth'))
    if Stalk_Surface_Above_Ring=='Fibrous':
        Stalk_Surface_Above_Ring=0
    elif Stalk_Surface_Above_Ring=='Scaly':
        Stalk_Surface_Above_Ring=3
    elif Stalk_Surface_Above_Ring=='Silky':
        Stalk_Surface_Above_Ring=1
    else:
        Stalk_Surface_Above_Ring=2
        
        
    Stalk_Surface_Below_Ring= st.selectbox('Stalk Surface Below Ring',('Fibrous','Scaly','Silky','Smooth'))
    if Stalk_Surface_Below_Ring=='Fibrous':
        Stalk_Surface_Below_Ring=0
    elif Stalk_Surface_Below_Ring=='Scaly':
        Stalk_Surface_Below_Ring=3
    elif Stalk_Surface_Below_Ring=='Silky':
        Stalk_Surface_Below_Ring=1
    else:
        Stalk_Surface_Below_Ring=2
        
        
    Stalk_Color_Above_Ring = st.selectbox('Stalk Color Above Ring',('Brown','Buff','Cinnamon','Gray','Orange','Pink','Red','White','Yellow'))
    if Stalk_Color_Above_Ring=='Brown':
        Stalk_Color_Above_Ring=4
    elif Stalk_Color_Above_Ring=='Buff':
        Stalk_Color_Above_Ring=0
    elif Stalk_Color_Above_Ring=='Cinnamon':
        Stalk_Color_Above_Ring=1
    elif Stalk_Color_Above_Ring=='Gray':
        Stalk_Color_Above_Ring=3
    elif Stalk_Color_Above_Ring=='Orange':
        Stalk_Color_Above_Ring=5
    elif Stalk_Color_Above_Ring=='Pink':
        Stalk_Color_Above_Ring=6
    elif Stalk_Color_Above_Ring=='Red':
        Stalk_Color_Above_Ring=2
    elif Stalk_Color_Above_Ring=='White':
        Stalk_Color_Above_Ring=7
    else:
        Stalk_Color_Above_Ring=8
        
    
    Stalk_Color_Below_Ring = st.selectbox('Stalk Color Below Ring',('Brown','Buff','Cinnamon','Gray','Orange','Pink','Red','White','Yellow'))
    if Stalk_Color_Below_Ring=='Brown':
        Stalk_Color_Below_Ring=4
    elif Stalk_Color_Below_Ring=='Buff':
        Stalk_Color_Below_Ring=0
    elif Stalk_Color_Below_Ring=='Cinnamon':
        Stalk_Color_Below_Ring=1
    elif Stalk_Color_Below_Ring=='Gray':
        Stalk_Color_Below_Ring=3
    elif Stalk_Color_Below_Ring=='Orange':
        Stalk_Color_Below_Ring=5
    elif Stalk_Color_Below_Ring=='Pink':
        Stalk_Color_Below_Ring=6
    elif Stalk_Color_Below_Ring=='Red':
        Stalk_Color_Below_Ring=2
    elif Stalk_Color_Below_Ring=='White':
        Stalk_Color_Below_Ring=7
    else:
        Stalk_Color_Below_Ring=8
        
    
    Ring_Number= st.selectbox('Ring Number',('None','One','Two'))
    if Ring_Number=='None':
        Ring_Number=0
    elif Ring_Number=='One':
        Ring_Number=1
    else:
        Ring_Number=2
        
    
    Ring_Type= st.selectbox('Ring Type',('Cobwebby','Evanescent','Flaring','Large','None','Pendant','Sheathing','Zone'))
    if Ring_Type=='Cobwebby':
        Ring_Type=0
    elif Ring_Type=='Evanescent':
        Ring_Type=1
    elif Ring_Type=='Flaring':
        Ring_Type=2
    elif Ring_Type=='Large':
        Ring_Type=3
    elif Ring_Type=='None':
        Ring_Type=4
    elif Ring_Type=='Pendant':
        Ring_Type=5
    elif Ring_Type=='Sheathing':
        Ring_Type=6
    else:
        Ring_Type=7
        
    
    Spore_Print_Color= st.selectbox('Spore Print Color',('Black','Brown','Buff','Chocolate','Green','Orange','Purple','White','Yellow'))
    if Spore_Print_Color=='Black':
        Spore_Print_Color=2
    elif Spore_Print_Color=='Brown':
        Spore_Print_Color=3
    elif Spore_Print_Color=='Buff':
        Spore_Print_Color=0
    elif Spore_Print_Color=='Chocolate':
        Spore_Print_Color=1
    elif Spore_Print_Color=='Green':
        Spore_Print_Color=5
    elif Spore_Print_Color=='Orange':
        Spore_Print_Color=4
    elif Spore_Print_Color=='Purple':
        Spore_Print_Color=6
    elif Spore_Print_Color=='White':
        Spore_Print_Color=7
    else:
        Spore_Print_Color=8
  

    Population= st.selectbox('population',('Abundant','Clustered','Numerous','Scattered','Several','Solitary'))
    if Population=='Abundant':
        Population=0
    elif Population=='Clustered':
        Population=1
    elif Population=='Numerous':
        Population=2
    elif Population=='Scattered':
        Population=3
    elif Population=='Several':
        Population=4
    else:
        Population=5
    
    Habitat= st.selectbox('Habitat',('Grasses','Leaves','Meadows','Paths','Urban','Waste','Woods'))
    if Habitat=='Grasses':
        Habitat=1
    elif Habitat=='Leaves':
        Habitat=2
    elif Habitat=='Meadows':
        Habitat=3
    elif Habitat=='Paths':
        Habitat=4
    elif Habitat=='Urban':
        Habitat=5
    elif Habitat=='Waste':
        Habitat=6
    else:
        Habitat=0
    
    
    data= {'cap-shape':Cap_Shape, 'cap-surface':Cap_Surface, 'cap-color':Cap_Color, 'bruises':Bruises, 'odor':Odor,
       'gill-spacing':Gill_Spacing, 'gill-size':Gill_Size, 'gill-color':Gill_Color, 'stalk-shape':Stalk_Shape, 'stalk-root':Stalk_Root,
       'stalk-surface-above-ring':Stalk_Surface_Above_Ring, 'stalk-surface-below-ring':Stalk_Surface_Below_Ring,
       'stalk-color-above-ring':Stalk_Color_Above_Ring  , 'stalk-color-below-ring':Stalk_Color_Below_Ring , 'ring-number':Ring_Number,
       'ring-type':Ring_Type, 'spore-print-color':Spore_Print_Color, 'population':Population, 'habitat':Habitat}
    features= pd.DataFrame(data,index=[0])
    
    return features

  


# In[36]:


df= user_input_features()


# In[37]:


table= pd.read_csv('mushrooms.csv')


# In[38]:


table=table.drop(['veil-type','gill-attachment','veil-color'],axis=1)


# In[39]:


x= table.drop(['class'],axis=1)
y= table['class']


# In[40]:


X=x.apply(LabelEncoder().fit_transform)


# In[41]:



le= LabelEncoder()
Y=le.fit_transform(y)


# In[42]:


x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3)


# In[43]:


model=RandomForestClassifier(max_features='sqrt',n_estimators=10)


# In[44]:


model.fit(x_train,y_train)


# In[45]:


predict=model.predict(df)


# In[46]:


st.subheader('Predicted Type')


# In[47]:


st.write('Edible'if predict==0 else 'Poisonous')

