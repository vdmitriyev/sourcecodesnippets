%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Function that reads JSON and store it as struct
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [config] = FuncReadJSONConfigs(configFileName)

    % reading pure JSON file
    jsonFile = fopen (configFileName);
    json = '';
    while true
        line = fgetl(jsonFile);
        if line != -1
            json = strcat(json, line);
        else
            break;
        end;
    end;
    fclose (jsonFile);

    % parsing JSON
    parsedConfigs = parse_json(json);

	% converting JSON to struct
    config.airfoilName = 'TempName';
    hash = parsedConfigs{1};
    keys = fieldnames(hash);
    for k=1:length(keys)
        key = keys{k};
        value = getfield(hash, key);
        tempValue = value.value;
        if strcmp(value.type, 'array')
            tempValue = cell2mat(tempValue);
        end;
        config = setfield (config, key, tempValue);
    end;
end;
