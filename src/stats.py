normal_count = 0
jamming_count = 0
suspicious_count = 0


def update_stats(prediction):

    global normal_count
    global jamming_count
    global suspicious_count

    if prediction == "NORMAL":
        normal_count += 1

    elif prediction == "JAMMING":
        jamming_count += 1

    elif prediction == "SUSPICIOUS":
        suspicious_count += 1

    print(
        f"\rNORMAL={normal_count} | "
        f"JAMMING={jamming_count} | "
        f"SUSPICIOUS={suspicious_count}",
        end=""
    )