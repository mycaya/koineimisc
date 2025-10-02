import json
import os
import shutil

def process_json_file(file_path, finished_folder):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        previous_end = 0

        for i, item in enumerate(data):
            combined_texts = [obj['text'] for obj in item['combined_objects']]
            item['text'] = ' '.join(combined_texts).strip()

            if item['combined_objects']:
                first_obj = item['combined_objects'][0]
                last_obj = item['combined_objects'][-1]

                # Set start value
                item['start'] = first_obj.get('start', previous_end)
                if item['start'] is None:
                    item['start'] = previous_end + 2

                # Set end value
                item['end'] = last_obj.get('end')
                if item['end'] is None:
                    next_start = (
                        data[i + 1]['combined_objects'][0].get('start', item['start'] + 2)
                        if i + 1 < len(data) else item['start'] + 2
                    )
                    item['end'] = next_start

                # Update previous_end for the next iteration
                previous_end = item['end']

        finished_file_path = os.path.join(finished_folder, os.path.basename(file_path))
        with open(finished_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print(f"Successfully processed: {file_path}")
    except Exception as e:
        print(f"Failed to process: {file_path} due to {e}")

def main():
    toprocess_folder = os.path.join(os.getcwd(), 'toprocess')
    finished_folder = os.path.join(os.getcwd(), 'finished')

    if not os.path.exists(finished_folder):
        os.makedirs(finished_folder)

    for filename in os.listdir(toprocess_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(toprocess_folder, filename)
            process_json_file(file_path, finished_folder)

if __name__ == "__main__":
    main()
