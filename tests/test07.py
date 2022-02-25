from utility_codes.frequency_distribubtion_table import generate_frequency_distribution_table


if __name__ == '__main__':
    #     # dataset = []
    #     # generate_frequency_distribution_table(dataset)
    import re


    unclean_data = '''50     52     53     54     55     65     60     70     48     63
    74     40     46     59     68     44     47     56     49     58
    63     66     68     61     57     58     62     52     56     58'''

    clean_data = re.split('\s+', unclean_data)

    for i in range(len(clean_data)):
        clean_data[i] = int(clean_data[i])

    print(min(clean_data))
    print(max(clean_data))

    generate_frequency_distribution_table(
        dataset=clean_data,
        interval_range=5,
        is_exclusive=False
    )

    unclean_data = '''185

166

176

145

166

191

177

164

171

174

147

178

176

142

170

158

171

167

180

178

173

148

168

187

181

172

165

169

173

184

175

156

158

187

156

172

162

193

173

183

197

181

151

161

153

172

162

179

188

179'''

    clean_data = re.split('\s+', unclean_data)

    for i in range(len(clean_data)):
        clean_data[i] = int(clean_data[i])

    # print(sorted(clean_data))

    # generate_frequency_distribution_table(
    #     dataset=clean_data,
    #     interval_range=5,
    #     is_exclusive=True
    # )

    # dataset = [2, 4, 8, 11, 14, 16, 20, 28, 25, 40, 30, 48, 5, 22, 29, 13, 22, 17, 17, 7]
    #
    # # print(sorted(clean_data))
    #
    # generate_frequency_distribution_table(
    #     dataset=dataset,
    #     interval_range=5,
    #     is_exclusive=True
    # )
