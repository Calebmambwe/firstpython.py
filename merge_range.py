def merge_range(meeting):
    sorted_meetings = sorted(meeting)

    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meetings_start, last_merged_meetings_end = merged_meetings[-1]

        if (current_meeting_start <= last_merged_meetings_start):
            merged_meetings[-1] = (last_merged_meetings_start,max(last_merged_meetings_end, current_meeting_start))
        else:
            merged_meetings.append((current_meeting_start,current_meeting_end))
    return merged_meetings


