import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO

# Title of the Streamlit app
st.title("Upload and Display Images - Grouped and High Quality ")

# Instructions for the user
st.write("Please upload 6 images.")

# Upload six images
uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

# Ensure exactly 6 images are uploaded
if len(uploaded_files) != 6:
    st.warning("Please upload exactly 6 images.")
else:
    # Labels for the subplots
    labels = ['a', 'b', 'c', 'd', 'e', 'f']

    # Create a 2x3 grid of subplots
    fig, axs = plt.subplots(2, 3, figsize=(25, 20))

    # Loop through the uploaded files, axes, and labels to display images and add labels
    for ax, uploaded_file, label in zip(axs.flat, uploaded_files, labels):
        img = mpimg.imread(uploaded_file)
        ax.imshow(img)
        ax.axis('off')  # Hide the axis
        ax.annotate(label, xy=(0.05, 0.95), xycoords='axes fraction', fontsize=20,
                    fontweight='bold', color='white',
                    bbox=dict(facecolor='black', alpha=0.5, edgecolor='none'))

    # Adjust layout
    plt.tight_layout()

    # Display the combined image
    st.pyplot(fig)

    # Save the figure to a BytesIO object
    img_buffer = BytesIO()
    fig.savefig(img_buffer, format='png', dpi=350)
    img_buffer.seek(0)

    # Add a download button
    st.download_button(
        label="Download Combined Image",
        data=img_buffer,
        file_name='combined_image.png',
        mime='image/png'
    )
