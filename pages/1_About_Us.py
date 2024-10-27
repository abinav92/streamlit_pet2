import streamlit as st

st.set_page_config(page_title = "About Us 🤷")
st.title("About Us 🤷")
st.sidebar.success("Current page: About Us 🤷")

with st.expander("Scope"):
    st.write("The scope of this app is to provide information about getting a pet in Singapore")
with st.expander("Objectives"):
    st.markdown("""
                Provide the following information in a fun and easy manner:
                - What does it take to get a pet?
                - To adopt or buy a pet?
                - Where to get a pet if adoption was decided?
                - Find out more about getting a pet using the chatbot.
                """)
with st.expander("Features"):
    st.markdown("""
                - The overall app is designed in fun manner and easy language with lots of emojis to keep the users engaged.
                - The questionnaire to get a pet is designed in a fun manner. The constructive response provided in the end is by LLM and it is dynamic.
                - The questionnaire holds the last answer so the user can reconsider their choices, if they try it out 2nd time or more.
                - If you get all answers correct, you have a surprise effect that awaits!
                - Should you decide to get a pet the 2 options availble to you adoption/buying and its merits and demirts are are clearly laid out.
                - The dynamic maps can be used to locate the nearest pet adoption center.
                - The map has tooltip and pop-up with website information. 
                - All the adoption centers with and without physical store front are listed in a table with their website and the offered pets. 
                - A Chat bot interface is provided with all the necessary background information so users can find out about getting a pet.
                """)
with st.expander("Data Sources"):
    st.markdown("""
                
                A combination of webpages and PDF documents only from official sources.
                
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/getting-a-pet/getting-a-pet
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/getting-a-pet/animals-allowed-for-sale
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/getting-a-pet/what-to-consider-before-you-get-a-pet
                https://www.nparks.gov.sg/avs/animals/animal-welfare/animal-and-pets-welfare/code-of-animal-welfare-(for-pet-owners)
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/getting-a-pet/how-to-know-if-you-would-make-a-good-pet-owner
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/getting-a-pet/where-to-get-a-pet
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/getting-a-pet/pets-,-a-,-asthma
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/caring-for-your-pet/veterinary-care
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/caring-for-your-pet/sterilising-your-pet
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/caring-for-your-pet/training-and-socialisation
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/caring-for-your-pet/legal-and-communal-guidelines-for-owning-a-dog
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/licensing-a-pet/cat-and-dog-licensing
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/licensing-a-pet/dog-training
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/licensing-a-pet/insurance-coverage
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/licensing-a-pet/banker%E2%80%99s-guarantee
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/licensing-a-pet/pets-in-hdb-flats
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/licensing-a-pet/pets-in-private-premises
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/licensing-a-pet/pets-kept-for-breeding-or-sale-in-pet-farms-or-pet-shops
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/licensing-a-pet/pet-licensing-e-services
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/lost-and-found-pets/keep-your-pet-safe-with-you
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/lost-and-found-pets/microchipping-,-a-,-registration
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/lost-and-found-pets/what-to-do-if-your-pet-goes-missing
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/lost-and-found-pets/what-to-do-if-you-find-a-missing-pet
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/lost-and-found-pets/claiming-an-impounded-animal
                https://www.nparks.gov.sg/avs/pets/owning-a-pet/guidelines-on-dog-rehoming,-adoption,-training-and-rehabilitation/guidelines-on-dog-rehoming,-adoption,-training-and-rehabilitation
                """)

