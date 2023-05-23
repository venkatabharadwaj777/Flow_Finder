import streamlit as st


flow = ['start']

def in_transit(keys):
    
    st.write("Select the Event in IN Transit")
    radio5 = st.selectbox('Events',['select event',
        'Receive Part in Inventory',
        'Part/Initial Installation',
        'Receive part at MRO'
        ],key = keys)
    flow.append(radio5)
    st.info(flow)
    return radio5

def part_inven():
    st.write("Currently are you in Part In Inventory Stage")
    part_inven = st.selectbox('Events',['select event',
        'MRO Exchange and Ship',
        'Ship Part to MRO',
        'Issue part from Inventory',
        'Sell Part'],key = "inven")
    
    flow.append(part_inven)
    st.info(flow)
    
    return part_inven

def Installed():
    inst = st.radio('select Item',['Removal'],key='install')
    if inst == 'Removal':
        flow.append(inst)
        st.info(flow)
        return in_transit('new2')

def under_main():
    
    main = st.radio('Pick One Under Maintenance Event',['select event','MRO Repair and Ship','Scrap a Part'],key='maintence')
    
    if main == 'select event':
        pass
    
    elif main == 'MRO Repair and Ship':
        flow.append(main)
        st.info(flow)
        return in_transit('new1')
    
    elif main == 'Scrap a Part':
        flow.append(main)
        st.info(flow)
        st.write("Scrap Stage and Final Stage")
        

def final_code():


    user  = st.selectbox('Pick one',['Drag and select','Part Of OEM Inventory','Part of Inventory','Done'],key='inputdata')

    flow.append(user)
    st.info(flow)
    
    if user == 'Drag and select':
        st.write("Pick up one option")

    elif user == 'Part Of OEM Inventory':
        
        st.write("Event is Fullfill Order")
        radio = in_transit('new4')
        
        if radio == 'select event':
            pass
            
        elif radio == 'Receive Part in Inventory':
            par = part_inven()
            
            if par == 'select event':
                pass
            elif par == 'MRO Exchange and Ship' or 'Ship Part to MRO' or 'Issue part from Inventory' or 'Sell Part':
                st.write("Currenlty we are in In Transit Stage")
                radio1 = in_transit('new3')
                
                if radio1 == 'select event':
                    pass
                
                elif radio1 == 'Part/Initial Installation':
                    st.write("Installed Stage")
                    
                elif radio1 == 'Receive part at MRO':
                    under_main()
                    
                elif radio1 == 'Receive Part in Inventory':
                    st.write("Process is done Select another event")
                    
        elif radio == 'Part/Initial Installation':
            Installed()
        
        elif radio == 'Receive part at MRO':
            under_main()
                    
                    

        
    elif user == 'Part of Inventory':
        
        par = part_inven()
        if par == 'select event':
            pass
            
        elif par == 'MRO Exchange and Ship' or 'Ship Part to MRO' or 'Issue part from Inventory' or 'Sell Part':
            radio2 = in_transit('new5')
            
            if radio2 == 'select event':
                st.write('pick Event')
                
            if radio2 == 'Part/Initial Installation':
                flow.append(radio2)
                st.write("Installed Stage")
                
            elif radio2 == 'Receive part at MRO':
                flow.append(radio2)
                under_main()
            elif radio2 == 'Receive Part in Inventory':
                st.write("Process is done Select another event")
        
        
final_code()
