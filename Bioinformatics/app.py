# Import Libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Import the image
image =Image.open("dna-logo.jpg")
st.image(image, caption='DNA Logo', use_column_width=True)

st.write("""
## DNA Nucleotide Count Web App
***
""")

st.header('Enter DNA sequence')

# Enter the DNA sequence between quotes
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height=150)
sequence = sequence.splitlines()
#sequence 
sequence = sequence[1:] # Skipping the sequence name (first line)
sequence = ''.join(sequence) # Joining the sequence lines into a single string

st.write("""
*** 
""")

st.header('INPUT (DNA Query)')
st.text(sequence)

# DNA Nucleotide Count
st.header('OUTPUT (DNA Nucleotide Count)')

# Print Dictionary
st.subheader('1. Print Dictionary')

# Custom function for counting DNA nucleotides
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)
st.write(X)

# Print the text in readable format
st.subheader('2. Print Text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

# Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame(X.items(), columns=['nucleotide', 'count'])
#df = df.set_index('nucleotide')
st.write(df)

# Display Bar Chart using Altair
st.subheader('4. Display Bar Chart')    
p = alt.Chart(df).mark_bar().encode(
    x=alt.X('nucleotide', axis=alt.Axis(labelAngle=0)),  # 0 = horizontal
    y='count'
)
#p = p.properties(width=alt.Step(80))
st.altair_chart(p, use_container_width=True)