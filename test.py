

def create_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=landscape(letter))
    story = []
    section_data = [
        ("General Community Conditions!", [ ]),
        ("Model Home!", [
            "Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5",
            "Question 6",
            "Question 7",
            "Question 8",
            "Question 9",
            "Question 10",
        ]),
        ("Sales Team & Sales Center!", [
            "Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5",
            "Question 6",
            "Question 7",
            "Question 8",
            "Question 9",
            "Question 10",
        ]),
        ("Finished Inventory!", [
            "Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5",
            "Question 6",
            "Question 7",
            "Question 8",
            "Question 9",
            "Question 10",
        ]),
    ]

    for section, questions in section_data:
        question_table_data = [["Question", "Options"]]
        for question in questions:
            question_table_data.append([question, "Option 1", "Option 2", "Option 3", "Option 4", "Option 5"])

        question_table = Table(question_table_data, colWidths=[2*inch, 1*inch, 1*inch, 1*inch, 1*inch, 1*inch])
        question_table.setStyle(TableStyle([
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.blue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        story.append(Spacer(1, 0.5 * inch))
        story.append(question_table)

    # # Adding images
    # image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]  # Replace with your image paths
    # for image_path in image_paths:
    #     img = Image.open(image_path)
    #     img = img.resize((200, 150))
    #     story.append(Spacer(1, 0.5 * inch))
    #     story.append(img)

    doc.build(story)

if __name__ == "__main__":
    print("Enter")
    create_pdf("questions_and_images.pdf")
