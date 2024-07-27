import streamlit as st
import math

st.subheader("To hop")
to_hop = st.text_input("C",key="to_hop")
to_hop_s = st.button("Tinh to hop")
if to_hop_s:
    t = to_hop.split(" ")
    if len(t) > 1:
        C = 0
        for i in t[1:]:
            C += math.comb(int(t[0]), int(i))
        st.write(C)

st.subheader("Chinh hop")
chinh_hop = st.text_input("A",key="chinh_hop")
chinh_hop_s = st.button("Tinh chinh hop")
if chinh_hop_s:
    t = chinh_hop.split(" ")
    if t.len() == 1:
        A = math.perm(int(t[0]))
    elif len(t) > 1:   
        A = 0
        for i in t[1:]:
            A += math.perm(int(t[0]), int(i))
    st.write(A)
 
def knapsack(values, weights, W):
    N = len(values)
    K = [[0 for x in range(W + 1)] for x in range(N + 1)]
 
    for i in range(N + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
        st.write(str(i)+" "+str(K[i][W])) 
    return K[N][W]
 
st.subheader("Chiec Tui") 
values = st.text_input(label="values",key="ct_values")
weights = st.text_input(label="weights",key="ct_weights")
W = st.text_input("",key="ct_W")  
knapsack_s = st.button("Tinh knapsack")
if knapsack_s:
    values = values.split(" ")
    values = [int(x) for x in values]
    weights = values.split(" ")
    weights = [int(x) for x in weights]
    ss = knapsack(values, weights, int(W))

  